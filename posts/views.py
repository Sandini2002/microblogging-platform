from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post 

# Homepage view that shows all posts
def posts(request):
    all_posts = Post.objects.all().order_by('-created_at') 
    return render(request, 'posts.html', {'posts': all_posts})


#@login_required  # Ensure only logged-in users can create posts
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save yet
            post.author = request.user  # Set the author to the logged-in user
            post.save()  # Save the post to the database
            return redirect('posts')  # Redirect to the homepage after posting
    else:
        form = PostForm()  # Display an empty form for GET requests

    return render(request, 'create_post.html', {'form': form})