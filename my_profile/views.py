from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect("my_profile")  # Redirect to the profile page after login
    return render(request, "home.html")  # Show the home page for unauthenticated users

@login_required
def my_profile(request):
    # Render the profile page using base2.html
    return render(request, "base2.html")

