from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView, ListView, TemplateView

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt


from forum.models import Post
from forum.forms import PostModelForm

from django.http import HttpResponse

def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request,'post/detail.html', {'post': post})

def index(request):
    return render(request, 'index.html', {'título': 'Em Destaque'})
def ola(request):
    posts = Post.objects.all()
    context = {'posts_list':posts}
    return render (request, 'index.html', context)

class PostDetailView(DetailView):

    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'

def get_all_posts(request):
    posts = list(Post.objects.values('pk','body_text', 'pub_date'))
    data = {'success': True, 'posts': posts}
    json_data= json.dumps(data, indent=1, cls=DjangoJSONEncoder)
    response = HttpResponse(json_data, content_type='application/json')
    response['Acess-Control-Allow-Origin']='*' #requisição de qualquer origem

    return response

def get_post(request, post_id):
    post = Post.objects.filter(pk=post_id).values('pk', 'body_text', 'pub_date').first()
    data = {'success': True, 'post': post}
    status=200
    if post is None:
        data = {'success': False, 'error': 'Post ID não existe'}
        status=404
    response = HttpResponse(json.dumps(data, indent=1, cls=DjangoJSONEncoder), content_type='application/json', status=status)
    response['Acess-Control-Allow-Origin']='*'
    return response

class PostCreateView(CreateView):
    model = Post
    template_name = 'index.html'
    fields = ('post_title', 'body_text', )
    success_url = reverse_lazy('posts_all')

@csrf_exempt
def create_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post_title = data.get('post_title')
        body_text= data.get('body_text')
        if body_text is None:
            data = {'success': False, 'error': 'Texto do post inválido.'}
            status = 400
        if post_title is None:
            data = {'success': False, 'error': 'Título do post inválido.'}
            status = 400
        else:
            post= Post(post_title=post_title, body_text=body_text)
            post.save()
            post_data= Post.objects.filter(pk=post.id).values('pk','post_title', 'body_text', 'pub_date').first()
            data = {'success': True, 'post': post_data}
            status=201
    response= HttpResponse(json.dumps(data, indent=1, cls=DjangoJSONEncoder), content_type='application/json', status=status)
    response['Acess-Control-Allow-Origin']='*'
    return response

class SobreTemplateView(TemplateView):
    template_name= '/index.html'
    
def post_create_modal(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status = 204,
                headers={
                    'HX-Trigger': json.dumps({
                        'postListChanged': None
                    })
                })
    else:
        form = PostModelForm()
    return render(request, 'post/post_modal_form.html',{'form': form})