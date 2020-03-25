"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls"), name='home'),
    path("api/", include("api.urls"), name='api'),
    path("course/", include("course.urls"), name='course'),
    path("search/", include("search.urls"), name='search'),
    path("post/", include("post.urls"), name='post'),
    path("user/", include("user.urls"), name='user'),
    path("community/", include("community.urls"), name='community'),
    path("feedback/", include("feedback.urls"), name='feedback'),
]
