from django.urls import path
from .views import test,register,login_user,home,logout_user

from .views import create_blog_post, my_blog_posts, blog_posts_by_category,blog_post_list

urlpatterns = [
  
]
urlpatterns = [

    path('test/',test,name='test'),
    path('register/',register,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('',home,name='home'),
    path('create/', create_blog_post, name='create_blog_post'),
    path('my_posts/', my_blog_posts, name='my_blog_posts'),
    path('category/<int:category_id>/', blog_posts_by_category, name='blog_posts_by_category'),
    path('blog_posts/', blog_post_list, name='blog_post_list'),
    
]
    