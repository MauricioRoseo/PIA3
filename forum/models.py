from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.TextField('Titulo do Post')
    body_text = models.TextField('Texto Principal')
    pub_date = models.DateTimeField('Data da Publicação', auto_now=True)
