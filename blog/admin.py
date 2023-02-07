from django.contrib import admin

# Register your models here.

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    search_fields = ['title', 'content']
    list_filter = ['title', 'content']

admin.site.register(Blog, BlogAdmin)