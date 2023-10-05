from django.urls import path

from forum.views import (index, ola, post_show, PostDetailView,get_all_posts, get_post, PostCreateView, create_post, post_create_modal)

urlpatterns = [
    path('', index, name="index"),
    path('index/', index, name="index"),
    path('ola/', ola, name="ola"),
    path('post/<int:post_id>', post_show, name="exibe_post"),
    path('post/<int:pk>/show', PostDetailView.as_view(), name='post_detail'),
    path('api/posts', get_all_posts, name="posts_data"),
    path('api/posts/<int:post_id>', get_post, name='post_data'),
    path('post_add/', PostCreateView.as_view(), name='post_add'),
    path('api/index', create_post, name='creat_post_data'),
    path('index/', post_create_modal, name='post_modal_add'),
]