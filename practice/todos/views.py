from django.shortcuts import render
from .form import TodoForms

# Create your views here.

def index(request):
    print('index 함수 도착')
    form = TodoForms()
    context = {
        'form':form,
    }
    return render(request, 'todos/index.html', context)


def create(request):
    print('create 함수 도착')
    return render(request, 'todos/create.html')