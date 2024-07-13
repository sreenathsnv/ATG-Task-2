from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager

class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    city = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    zipcode = models.TextField(max_length=50)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.first_name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def truncated_summary(self):
        return ' '.join(self.summary.split()[:15]) + '...' if len(self.summary.split()) > 15 else self.summary
