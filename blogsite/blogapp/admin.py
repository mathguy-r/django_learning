from django.contrib import admin
from .models import Author, BlogContent

# Register your models here.

admin.site.register(Author)
admin.site.register(BlogContent)
