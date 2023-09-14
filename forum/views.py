from django.shortcuts import render

from forum.models import Post

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'título': 'Em Destaque'})
def ola(request):
    posts = Post.objects.all()
    context = {'posts_list':posts}
    return render (request, 'index.html', context)