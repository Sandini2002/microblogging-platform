from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),  # Example route for the homepage
    path('post/create/', views.create_post, name='create_post'),  # Example route for creating posts
]