from datetime import datetime
from django import forms
from forum.models import Post


class PostModelForm(forms.ModelForm):
    error_css_class = "alert-danger"
        
    class Meta:
        model = Post
        fields = ('post_title', "body_text",)
        labels = {"body_text": "",}