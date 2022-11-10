from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import People
from animal.models import Animal, ShoppingList, TaskList
from .forms import UserForm, PeopleForm, AddressForm, ProductForm, TaskForm


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
    #import ipdb ; ipdb.set_trace()
    #shopping_list = shopping_list.products.all()
    
    #shopping_list = ShoppingList.objects.filter(animal_id=Animal.objects.filter(id=1).first())
    return render(request, 'shooping_list.html', {'list': shopping_list})

def register_product(request):
    form = ProductForm()
    if request.method == 'POST':
        import ipdb ; ipdb.set_trace()
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


def task_list(request):
    shopping_list = TaskList.objects.filter(animal_id=1)
    #import ipdb ; ipdb.set_trace()
    #shopping_list = shopping_list.products.all()
    
    #shopping_list = ShoppingList.objects.filter(animal_id=Animal.objects.filter(id=1).first())
    return render(request, 'task_list.html', {'list': shopping_list})


def register_task(request):
    form = TaskForm()
    if request.method == 'POST':
        import ipdb ; ipdb.set_trace()
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