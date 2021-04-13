from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_created=True, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_articles')
