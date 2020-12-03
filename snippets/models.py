from django.db import models
from django.contrib.auth.models import User


class Snippet(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
