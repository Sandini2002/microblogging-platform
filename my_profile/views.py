from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from posts.models import Post, Comment, Like
from posts.forms import PostForm  # Correct the import to reference the 'posts' app

def home(request):
    """View for the home page"""
    return render(request, 'base2.html')

def posts(request):
    return render(request, 'base2.html')

@login_required
def my_profile(request):
    """View for the current user's profile"""
    return redirect('my_profile', username=request.user.username)

@login_required
def profile_view(request, username=None):
    """View for any user's profile"""
    if not username:
        raise Http404("No User matches the given query.")
    
    profile_user = get_object_or_404(User, username=username)
    
    # Get user posts
    user_posts = Post.objects.filter(author=profile_user).order_by('-created_at')
    
    # Get posts liked by the user (if your Like model has a user field)
    liked_posts = Post.objects.filter(likes__user=profile_user).distinct().order_by('-created_at')
    
    # Get user comments
    user_comments = Comment.objects.filter(author=profile_user).order_by('-created_at')
    
    context = {
        'profile_user': profile_user,
        'user_posts': user_posts,
        'liked_posts': liked_posts,
        'user_comments': user_comments,
    }
    
    return render(request, 'profile.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('posts')  # Redirect to the posts page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})