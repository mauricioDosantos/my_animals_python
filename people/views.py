from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import People, Address
from animal.models import Animal, ShoppingList, TaskList, Vaccine, VaccineCard, Task, Product
from .forms import (
    UserForm, PeopleForm, AddressForm,
    ProductForm, TaskForm, VaccineForm,
    AnimalForm
)


def people_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main')
    return 


@login_required
def people_logout(request):
    logout(request)
    return redirect('main_external_page')


def create_user(request):
    is_active = True
    is_staff = False
    is_superuser = False
    user_f = UserForm()
    people_f =  PeopleForm()
    address_f = AddressForm()

    if request.method == 'POST':
        data = request.POST
        user_f = UserForm(data)
        people_f =  PeopleForm(data)
        address_f = AddressForm(data)
        if user_f.is_valid():
            user_f.is_active = is_active
            user_f.is_staff = is_staff
            user_f.is_superuser = is_superuser
            user_s = user_f.save()
            if people_f.is_valid():
                # import ipdb ; ipdb.set_trace()
                people_f.user = user_s
                people_s = people_f.save()
                if address_f.is_valid():
                    address_f.people_id = people_s
                    address_f.save()
            return redirect('main')

    return render(
        request, 'register.html',
        {'user_form': user_f, 'people_form': people_f, 'address_form': address_f}
    )


def main(request):
    return render(request, 'main.html')

def shooping_list(request):
    shopping_list = ShoppingList.objects.filter(animal_id=1)
    product = []
    for item in shopping_list:
        for i in item.products.all():
            product.append(i)
    return render(request, 'shooping_list.html', {'list': shopping_list.first(), 'product': product})

def register_product(request):
    form = ProductForm()
    if request.method == 'POST':
        ref_date = request.POST['ref_date']
        form = ProductForm(request.POST)
        if form.is_valid():
            form_s = form.save()
            shopping = ShoppingList(ref_date=ref_date, animal_id=Animal.objects.filter(id=1).first())
            shopping.save()
            shopping.products.add(form_s)
            shopping.save()

            return redirect('shooping_list')
    return render(request, 'register_product.html', {'form': form})


def delete_product(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('shooping_list')


def task_list(request):
    shopping_list = TaskList.objects.filter(animal_id=1)
    tasks = []
    for item in shopping_list:
        for i in item.tasks.all():
            tasks.append(i)
    return render(request, 'task_list.html', {'list': shopping_list.first(), 'tasks': tasks})


def register_task(request):
    form = TaskForm()
    if request.method == 'POST':
        ref_date = request.POST['ref_date']
        form = TaskForm(request.POST)
        if form.is_valid():
            form_s = form.save()
            shopping = TaskList(ref_date=ref_date, animal_id=Animal.objects.filter(id=1).first())
            shopping.save()
            shopping.tasks.add(form_s)
            shopping.save()

            return redirect('task_list')
    return render(request, 'register_task.html', {'form': form})


def delete_task(request, id):
    Task.objects.filter(id=id).delete()
    return redirect('task_list')


def my_profile(request):
    people = People.objects.filter(id=1).first()
    user = people.user
    address = Address.objects.filter()
    return render(request, 'profile.html', {'people': people, 'user': user, 'address': address})


def vaccine(request):
    vaccine_l = VaccineCard.objects.filter(animal_id=1)
    vaccine = []
    for item in vaccine_l:
        for i in item.vaccines.all():
            vaccine.append(i)
    return render(request, 'vaccine_portfolio.html', {'vaccine_l': vaccine_l.first(),'vaccine': vaccine})


def register_vaccine(request):
    form = VaccineForm()
    if request.method == 'POST':
        ref_date = request.POST['ref_date']
        form = VaccineForm(request.POST)
        if form.is_valid():
            
            form_s = form.save()
            vaccine = VaccineCard(ref_date=ref_date, animal_id=Animal.objects.filter(id=1).first())
            vaccine.save()
            vaccine.vaccines.add(form_s)
            vaccine.save()

            return redirect('vaccine')
    return render(request, 'register_vaccine.html', {'form': form})


def delete_vaccine(request, id):
    Vaccine.objects.filter(id=id).delete()
    return redirect('vaccine')


def main_external(request):
    return render(request, 'main_external.html')


def pricing(request):
    return render(request, 'pricing.html')


def pet_list(request):
    animal = Animal.objects.filter(people_id=1).all()
    return render(request, 'pet_list.html', {'animal': animal})

def delete_pet(request, id):
    Animal.objects.filter(id=id).delete()
    return redirect('pet_list')


def pet_register(request):
    form = AnimalForm()
    if request.method == 'POST':

        form = AnimalForm(request.POST)

        animal = Animal(
            name=request.POST['name'], birthday=request.POST['birthday'],
            breed=request.POST['breed'], weight=request.POST['weight'],
            height=request.POST['height'], people_id=People.objects.filter(id=1).first()
        )
        animal.save()
        return redirect('pet_list')
    return render(request, 'register_pet.html', {'form': form})