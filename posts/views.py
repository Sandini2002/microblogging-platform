from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
from .models import Post, Comment, Like
from django.contrib.auth import logout

# Homepage view that shows all posts
def posts(request):
    # Get all posts ordered by most recent
    all_posts = Post.objects.all().order_by('-created_at') 
    return render(request, 'posts.html', {'posts': all_posts})

# Create a new post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            post = form.save(commit=False)  # Don't save yet
            post.author = request.user  # Set the author to the logged-in user
            post.save()  # Save the post to the database
            return redirect('posts')  # Redirect to the homepage after posting
    else:
        form = PostForm()  # Display an empty form for GET requests

    return render(request, 'create_post.html', {'form': form})

# Delete a post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)  # Ensure the post belongs to the user
    if request.method == 'POST':
        post.delete()
        return redirect('posts')  # Redirect to the homepage after deletion
    return redirect('posts')

# Update a post
@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)  # Ensure the post belongs to the user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')  # Redirect to the homepage after updating
    else:
        form = PostForm(instance=post)  # Pre-fill the form with the existing post data

    return render(request, 'update_post.html', {'form': form})

# Add a comment to a post or another comment
@login_required
def add_comment(request, post_id=None, comment_id=None):
    if post_id:
        # Adding a comment to a post
        post = get_object_or_404(Post, id=post_id)
        parent_comment = None
    elif comment_id:
        # Adding a reply to a comment
        parent_comment = get_object_or_404(Comment, id=comment_id)
        post = parent_comment.post  # Associate the reply with the same post as the parent comment

    if request.method == 'POST':
        content = request.POST.get('comment_content')
        if content:
            Comment.objects.create(
                post=post,
                parent_comment=parent_comment,  # Set the parent comment for replies
                author=request.user,
                content=content
            )
    return redirect('posts')  # Redirect to the homepage after adding a comment or reply

# Like a post or comment
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()  # Unlike if already liked
    return redirect('posts')

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    like, created = Like.objects.get_or_create(user=request.user, comment=comment)
    if not created:
        like.delete()  # Unlike if already liked
    return redirect('posts')

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)  # Ensure the user owns the comment
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('posts')  # Redirect to the homepage after editing
    else:
        form = CommentForm(instance=comment)  # Pre-fill the form with the existing comment data
    return render(request, 'edit_comment.html', {'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)  # Ensure the user owns the comment
    if request.method == 'POST':
        comment.delete()
        return redirect('posts')  # Redirect to the homepage after deletion
    return redirect('posts')

# Profile views
@login_required
def my_profile(request):
    """Redirect to the current user's profile"""
    return redirect('profile', username=request.user.username)

def logout_view(request):
    logout(request)
    return redirect('home.html')

@login_required
def profile_view(request, username):
    """View for any user's profile"""
    profile_user = get_object_or_404(User, username=username)
    
    # Get user posts
    user_posts = Post.objects.filter(author=profile_user).order_by('-created_at')
    
    # Get posts liked by the user
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