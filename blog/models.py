from __future__ import unicode_literals
from django.db import models
import time

class Article(models.Model):
    title = models.CharField(max_length = 32,default = 'Title')
    content = models.TextField(null=True)
    content_one = models.TextField(null = True)
    def __str__(self):
        return self.title
