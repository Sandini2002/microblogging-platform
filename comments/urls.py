from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.comment, name='comment'),  # Example route for creating posts
]