from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
#https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types(doc refference)

class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(auto_now_add=False, auto_now=False,
                                 default=timezone.now, null=True,blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        #     self.save()
