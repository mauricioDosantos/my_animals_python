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

from people.views import (
    main, shooping_list, register_product, task_list,
    register_task, my_profile, vaccine, register_vaccine,
    delete_task, delete_product, delete_vaccine, main_external,
    pricing, pet_list, delete_pet, pet_register
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', include('people.urls')),
    path('', main, name='main'),
    path('shopping_list/', shooping_list, name='shooping_list'),
    path('delete_product/<int:id>', delete_product, name='delete_prodcut'),
    path('register_product/', register_product, name='register_product'),
    path('task_list/', task_list, name='task_list'),
    path('register_task/', register_task, name='register_task'),
    path('profile/', my_profile, name='profile'),
    path('vaccine/', vaccine, name='vaccine'),
    path('register_vaccine/', register_vaccine, name='register_vaccine'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('delete_vaccine/<int:id>', delete_vaccine, name='delete_vaccine'),
    path('main_external/', main_external, name='main_external'),
    path('pricing/', pricing, name='pricing'),
    path('pet_list/', pet_list, name='pet_list'),
    path('delete_pet/<int:id>', delete_pet, name='delete_pet'),
    path('pet_register/', pet_register, name='pet_register'),
]