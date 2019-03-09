from django.shortcuts import render
from .models import Animal, Question
# Create your views here.
from django.views import generic
from django.views import View

from django.http import *
from . import variables
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout


class Questions(View):

    def get(self, request):
        questions = Question.objects.all()
        return HttpResponse(questions)


class Contact(View):

    def get(self, request):
        return render(request, 'store/contact-page.html')

    def post(self, request):
        data = request.POST.copy()
        question = Question(email=data.get('email'), question=data.get('question'))
        question.save()
        return HttpResponse('ok')


class AnimalView(generic.ListView):
    template_name = 'store/animals.html'
    context_object_name = 'animals'

    def get_queryset(self):
        return Animal.objects.Queryset().order_by('name')


def logout_user(request):
    logout(request)
    print('logout')
    return render(request, 'store/landing_page.html', {'breeds': context_navbar()})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'store/login.html')
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return render(request, 'store/profile.html', {'user': user})
    return render(request, 'store/error.html', {'error': 'No such user'})


def index(request):
    print('index')

    return render(request, 'store/landing_page.html', {'breeds': context_navbar()})


def animals(request):
    fields_query = request.GET.dict()
    arguments = {}
    for k, v in fields_query.items():
        if v and not v == 'None':
            arguments[k] = v

    print(f'arguments: {arguments}')
    animal_list = []
    if arguments:
        print(f'ima e go {arguments}')
        try:
            animal_list = Animal.objects.all().filter(**arguments)
            print(animal_list)
            return render(request, 'store/animals.html', {'animals': animal_list, 'breeds': context_navbar()})
        except Exception as exception:
            return render(request, '/store/error.html', {'error': exception, 'breeds': context_navbar()})
        print('search_breed')
        print(breed_id)
    print('animals')
    animal_list = Animal.objects.all()
    return render(request, 'store/animals.html', {'animals': animal_list, 'breeds': context_navbar()})


def delete(request, animal_id):
    try:
        Animal.objects.all().filter(id=animal_id).delete()
        return HttpResponseRedirect('/store')
    except Exception as exception:
        return render(request, 'store/error.html', {'error': exception})

def delete_animal(request, animal_id):
    if not request.user:
        return HttpResponseRedirect('store/login')
    elif not request.user.has_perm('store.delete_animal'):
        return render(request, 'store/delete.html', {'permission': 'You have no permissions to delete'})
    else:
        return render(request, 'store/delete.html', {'obj': animal_id, 'breeds': variables.all_breeds})


def animal(request, animal_id):
    print('animal')
    animal_obj = Animal.objects.get(pk=animal_id)
    return render(request, 'store/animal.html', {'animal': animal_obj, 'breed': animal_obj.get_breed(), 'color': animal_obj.get_color(), 'breeds': context_navbar(), 'user': request.user})



def animal_edit(request, animal_id):
    if request.method == 'GET':
        try:
            animal = Animal.objects.all().filter(id=animal_id)[0]
            breed_str = list(filter(lambda kvp: kvp[0]==animal.breed, variables.all_breeds))[0]
            color_str = list(filter(lambda kvp: kvp[0]==animal.color, variables.basic_colors))[0]
            kind_str = list(filter(lambda kvp: kvp[0]==animal.kind, variables.KIND_ANIMAL_CHOICES))[0]
            print(breed_str[1])
            return render(request, 'store/edit-animal.html', {'animal': animal, 'kinds': variables.KIND_ANIMAL_CHOICES, 'breeds': variables.all_breeds, 'breed_str': breed_str[1], 'color_str': color_str[1], 'kind_str': kind_str[1], 'colors': variables.basic_colors})
        except Exception as exception:
            return render(request, 'store/error.html', {'error': exception})
    elif request.method == 'POST':
        try:
            data = request.POST.copy()
            print(data.get('image'))
            name = data.get('name')
            kind = data.get('kind')
            image = None
            age = data.get('age')
            breed = data.get('breed')
            color = data.get('color')
            price = data.get('price')
            if data.get('image'):
                image = request.FILES.get('image')
                Animal.objects.all().filter(id=animal_id).update(name=name, age=age, color= color, kind=kind, breed=breed, price=price, image=image)
            else:
                Animal.objects.all().filter(id=animal_id).update(name=name, age=age, color= color, kind=kind, breed=breed, price=price)
            return HttpResponseRedirect('/store/animals/'+animal_id+'/')
        except Exception as exception:
            return render(request, 'store/error.html', {'error': exception})



def create_animal(request):
    print('create_animal')
    if request.method == 'GET':
        return render(request, 'store/create-animal.html', {'kinds': variables.KIND_ANIMAL_CHOICES, 'breeds': variables.all_breeds,'colors': variables.basic_colors})
    elif request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        age = data.get('age')
        color = data.get('color')
        breed = data.get('breed')
        image = request.FILES.get('image')
        kind = data.get('kind')
        price = data.get('price')
        animal = Animal(name= name, age=age, color=color, breed=breed, image=image, kind=kind, price=price)
        animal.save()
        return HttpResponseRedirect('/store/animals/')



def context_navbar():
    return variables.all_breeds


def search(request):
    print('search')
    return render(request, 'store/search.html', {
        'breeds': variables.all_breeds,
        'kinds': variables.KIND_ANIMAL_CHOICES,
        'colors': variables.basic_colors,
        'ages': variables.age_groups

                                                 })