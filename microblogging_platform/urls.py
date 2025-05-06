"""
URL configuration for microblogging_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts import views as post_views
from my_profile import views as profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_views.home, name='home'),  # Root URL for unauthenticated users
    path('profile/<str:username>/', post_views.profile_view, name='profile'),
    path('my_profile/', post_views.my_profile, name='my_profile'),
    path('logout/', post_views.logout_view, name='logout'),  # Add this view
    path('', include('posts.urls')),
    path('', include('accounts.urls')),  # Include accounts app URLs
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
