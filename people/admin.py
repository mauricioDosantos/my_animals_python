from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .models import People, Plan, MyPlan, Address

admin.site.register(People)
admin.site.register(Plan)
admin.site.register(MyPlan)
admin.site.register(Address)