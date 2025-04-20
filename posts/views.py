from django.shortcuts import render

# Create your views here.
def posts(request):
    # Example logic for the homepage
    return render(request, 'posts.html', {'message': 'Welcome to the postspage!'})

def create_post(request):
    # Example logic for the postspage
    return render(request, 'posts.html', {'message': 'Welcome to the create post page!'})
    
posts = Post.objects.all()