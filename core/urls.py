"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from people.views import main, shooping_list, register_product, task_list, register_task


urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', include('people.urls')),
    path('', main, name='main'),
    path('shopping_list/', shooping_list, name='shooping_list'),
    path('register_product/', register_product, name='register_product'),
    path('task_list/', task_list, name='task_list'),
    path('register_task/', register_task, name='register_task'),
]
