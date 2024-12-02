from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

"""
Vistas de la aplicación de tareas
El decorador @login_required se encarga de redirigir a la página de login si el usuario no está autenticado
"""

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/tasks/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Mostrar todas las tareas
@login_required
def list_tasks(request):
    tasks = Task.objects.filter(user=request.user)  # Filtra por usuario
    completed = request.GET.get('completed')
    pending = request.GET.get('pending')
    if completed and not pending:
        tasks = tasks.filter(completed=True)
    if pending and not completed:
        tasks = tasks.filter(completed=False)
    return render(request, 'tasks.html', {"tasks": tasks})

# Crear una tarea
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Asigna el usuario autenticado
            task.save()
            return redirect('/tasks/')
    else:
        form = TaskForm()
    return render(request, 'edit_task.html', {'form': form})

# Eliminar una tarea
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Filtra por usuario
    task.delete()
    return redirect('/tasks/')

# Editar una tarea
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Filtra por usuario
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

# Marcar una tarea como completada
@login_required
def task_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Filtra por usuario
    task.completed = not task.completed
    task.save()
    return redirect('/tasks/')