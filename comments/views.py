from django.shortcuts import render

# Create your views here.
def comment(request):
    return render(request, 'comment.html', {'message': 'Welcome to the homepage!'})