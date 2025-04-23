from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')



def user_register(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return JsonResponse({'success': False, 'message': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return JsonResponse({
            'success': True,
            'message': 'Account created successfully!',
            'redirect_url': '/login/'  # Adjust if you’ve named the login URL differently
        })

    # Regular GET request to render the form
    return render(request, 'register.html')



def user_login(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return JsonResponse({
                'success': True,
                'message': 'Login successful!',
                'redirect_url': '/posts'  # Redirect to the homepage after login
            })
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password'})

    # Regular GET request to render the form
    return render(request, 'login.html')