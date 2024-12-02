from django.contrib import admin
from django.urls import path, include
from tasks.views import register
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', register, name='register'),
    path('tasks/', include('tasks.urls')),
    path(',accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/tasks/', permanent=True))  # Redirección desde la raíz a /tasks/
]