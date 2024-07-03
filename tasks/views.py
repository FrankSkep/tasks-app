from django.shortcuts import render, redirect
from .models import Task

def list_tasks(request):
    tasks = Task.objects.all() # Obtener lista de todos los objetos, orm
    return render(request, 'tasks.html', {"tasks":tasks})

def create_task(request):
    # Construyo objeto de la tarea con su clave-valor
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save() # Guardo la tarea en la db
    print(request.POST)
    return redirect('/tasks/')

def delete_task(request, task_id):
    task_delete = Task.objects.get(id=task_id)
    task_delete.delete()
    return redirect('/tasks/')