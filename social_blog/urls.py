"""social_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
# from django.contrib.auth.views import LoginView
# from django.contrib.auth import logout
from social_blog.views import Homepage
# from social_site.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/',LoginView.as_view(),name='login'),
    # path('logout/',logout,{'next_page':'/'},name='logout'),
    path('auth/',include('social_django.urls',namespace='social')),#for social login
    path('',Homepage.as_view(),name='home'),
    path('site/',include('social_site.urls',namespace='site')),
    path('site/',include('django.contrib.auth.urls')),
    path('post/',include('posts.urls',namespace='posts')),
    path('groups/',include('groups.urls',namespace='groups')),
]
