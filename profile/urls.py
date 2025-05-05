from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Existing URLs
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),  
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    
    # Profile URLs
    path('profile/', views.my_profile, name='my_profile'),  # Current user's profile
    path('profile/<str:username>/', views.profile_view, name='profile'),  # Any user's profile
    
    # Include the posts app URLs
    path('', include('posts.urls')),
]