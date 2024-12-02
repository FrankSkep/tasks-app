from django.db import models
from django.contrib.auth.models import User

# Modelo de una tarea
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Relación con el usuario