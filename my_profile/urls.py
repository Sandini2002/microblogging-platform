from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import posts  

urlpatterns = [
    # Existing URLs
    path('', posts, name='home'),

    # Profile URLs
    path('my_profile/', views.my_profile, name='my_profile'),  # Current user's profile
    path('base2.html', views.posts, name='posts'),  # Specific route for posts
    path('my_profile/<str:username>', views.my_profile, name='my_profile'),  # Current user's profile
    path('<str:username>/', views.profile_view, name='profile'),  # Any user's profile
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout')

    
    # Include the posts app URLs
    path('', include('posts.urls')),
]