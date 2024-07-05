from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import CustomUserManager
# Create your models here.


class CustomUserModel(AbstractBaseUser,PermissionsMixin):
    
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