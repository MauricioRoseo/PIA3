from django.shortcuts import render, get_object_or_404

from django.views.generic.detail import DetailView

from forum.models import Post

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