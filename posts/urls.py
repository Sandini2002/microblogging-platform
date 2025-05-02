from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),  # Example route for the homepage
    path('post/create/', views.create_post, name='create_post'),  # Example route for creating posts
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),  # Delete post route
    path('post/update/<int:post_id>/', views.update_post, name='update_post'),  # Update post route
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),  # Add comment to a post
    path('comment/<int:comment_id>/reply/', views.add_comment, name='add_reply'),  # Add a reply to a comment
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]