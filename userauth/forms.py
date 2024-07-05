
from django import forms
from .models import CustomUserModel

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['email','first_name','last_name','password','profile_picture','city','state','zipcode','is_patient','is_doctor']