from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    # tasks = Task.objects.all()
    # tasks = Task.objects.order_by('-date_task')[:2]
    tasks = Task.objects.order_by('-date_task')
    
    return render(request, 'main/index.html', {'title':'Головна сторінка сайта', 'tasks': tasks})
    # return HttpResponse("<h1>Головна</h1>")


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')

def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Уважно перевірте чи усі поля форми заповнені вірно'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_task.html', context)





