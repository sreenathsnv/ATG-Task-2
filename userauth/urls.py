from django.urls import path
from .views import test,register,login_user,home,logout_user
urlpatterns = [

    path('test/',test,name='test'),
    path('register/',register,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('',home,name='home'),
    
]
    