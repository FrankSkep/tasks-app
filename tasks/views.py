from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Mostrar todas las tareas
def list_tasks(request):
    tasks = Task.objects.all()  # Obtener todas las tareas
    
    # Obtener valor checkbox
    completed = request.GET.get('completed')
    pending = request.GET.get('pending')
    
    # Filtrado
    if completed and not pending:
        tasks = tasks.filter(completed=True)
    if pending and not completed:
        tasks = tasks.filter(completed=False)
    
    return render(request, 'tasks.html', {"tasks": tasks})

# Crear una tarea
def create_task(request):
    # Construyo objeto de la tarea con su clave-valor
    task = Task(title=request.POST['title'],
                description=request.POST['description'])
    task.save()  # Guardo la tarea en la db
    return redirect('/tasks/')

# Eliminar una tarea
def delete_task(request, task_id):
    task_delete = Task.objects.get(id=task_id)
    task_delete.delete()
    return redirect('/tasks/')

# Editar una tarea
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            # Redirige a la página de tareas después de editar
            return redirect('/tasks/')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form})

# Marcar una tarea como completada
def task_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    task.completed = True # Marca completada
    task.save()
    
    return redirect('/tasks/')