from django.contrib import admin

# Register your models here.
from .models import Category, Post, Comment, Like

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
