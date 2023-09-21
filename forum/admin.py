from django.contrib import admin
from forum.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','post_title', 'body_text', 'pub_date')
    list_filter = ('pub_date',)
# Register your models here.
