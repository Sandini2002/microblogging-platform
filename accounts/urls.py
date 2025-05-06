from django.urls import path
from . import views
from .views import user_register

urlpatterns = [
    path('', views.home, name='home'),
    path('user_login/', views.user_login, name='login'),  
    path('register/', user_register, name='register'),
    path('home/', views.home, name='home'),  
    
]