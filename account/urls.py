"""task URL Configuration

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
from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home_task, name="home_task"),
    path('register_des', views.register_des, name="register_des"),
    path('login_des', views.login_des, name="login_des"),
    path('sucess', views.sucess, name="sucess"),
    path("logout_des",views.logout_des,name="logout_des"),
    path("password", views.change_password, name='change_password'),
]