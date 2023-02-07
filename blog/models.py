from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.TextField()
    content = models.TextField()
