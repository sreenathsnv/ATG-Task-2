
from django import forms
from .models import CustomUserModel
from .models import BlogPost, Category

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['email','first_name','last_name','password','profile_picture','city','state','zipcode','is_patient','is_doctor']
    
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
