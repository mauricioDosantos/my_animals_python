from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

from .views import logout, create_user


urlpatterns = [
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', logout),
    path('create_user/', create_user),
]