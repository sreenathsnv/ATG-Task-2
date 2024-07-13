from django.contrib import admin

# Register your models here.

from .models import CustomUserModel, Category, BlogPost

admin.site.register(CustomUserModel)
admin.site.register(Category)
admin.site.register(BlogPost)