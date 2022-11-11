from django import forms

from django.contrib.auth.models import User
from .models import People, Address
from animal.models import Product, Task, Vaccine, Animal

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'username']


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['user', 'birthday', 'cpf']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['zip_code', 'street', 'city', 'complement', 'district', 'number']


class ProductForm(forms.ModelForm):
    ref_date = forms.DateTimeField(required=True)
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class TaskForm(forms.ModelForm):
    ref_date = forms.DateTimeField(required=True)
    class Meta:
        model = Task
        fields = ['name', 'description']


class VaccineForm(forms.ModelForm):
    ref_date = forms.DateTimeField(required=True)
    class Meta:
        model = Vaccine
        fields = ['name', 'dose', 'days_between_dose', 'description']


class AnimalForm(forms.ModelForm):
    people_id = forms.ImageField()
    class Meta:
        model = Animal
        fields = ['name', 'birthday', 'weight', 'height']