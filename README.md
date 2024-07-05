# <h1 align="center">Tasks App</h1>

Aplicacion web de lista de tareas desarrollada con Django, y base de datos PostgreSQL para almacenar y gestionar las tareas.

## <h2 align="center">Interfaz principal:</h2>
![ImagenInterfaz](https://raw.githubusercontent.com/FrankSkep/Tasks-App/main/tasks/static/preview/main_view.png)
## <h2 align="center">Interfaz de edicion:</h2>
![ImagenEdit](https://raw.githubusercontent.com/FrankSkep/Tasks-App/main/tasks/static/preview/edit_task.png)


## Características

- **Agregar Tareas**: Permite a los usuarios agregar nuevas tareas a la lista.
- **Visualización de Tareas**: Los usuarios pueden ver todas las tareas en la lista.
- **Edición de Tareas**: Permite a los usuarios editar las tareas existentes.
- **Eliminación de Tareas**: Los usuarios pueden eliminar las tareas de la lista.
- **Marcar como Completada**: Los usuarios pueden marcar una tarea como completada o volver a marcarla como pendiente según sea necesario.
- **Filtrado de Tareas**: Los usuarios pueden filtrar las tareas segun su estado (Completada o Pendiente), mostrando solo aquellas que necesitas ver en un momento dado.
- **Indicador de estado**: Podras visualizar el estado de cada tarea, en la esquina inferior izquierda, facilitando la identificación visual rápida de su estado actual.

## Requisitos

- Python 3.x
- Django 5.x o superior
- PostgreSQL
- psycopg2 (para la conexión de Django con PostgreSQL)

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/FrankSkep/Tasks-App
    cd Tasks-App
    ```

2. Crea un entorno virtual e instálalo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura la base de datos PostgreSQL.
    - Crea una base de datos en PostgreSQL.
    - Configura tus credenciales de la base de datos en `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario_postgres',
            'PASSWORD': 'tu_contraseña_postgres',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Aplica las migraciones para configurar la base de datos:
    ```sh
    python manage.py migrate
    ```


6. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Uso

1. Abre tu navegador web y ve a `http://127.0.0.1:8000/tasks/`.
2. Puedes agregar, ver, editar y eliminar tareas utilizando la interfaz de usuario.

## Estructura del proyecto

```plaintext
Tasks-App/
├── manage.py              # Script de Django para administrar el proyecto.
├── django_project/
│   ├── __init__.py
│   ├── settings.py        # Configuraciones del proyecto Django, incluyendo la configuración de la base de datos.
│   ├── urls.py            # Archivo de configuración de URLs del proyecto.
│   ├── wsgi.py            # Configuración para la implementación del proyecto con un servidor WSGI.
│   └── asgi.py
├── tasks/
│   ├── migrations/        # Archivos que gestionan los cambios en el esquema de la base de datos .
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Define el modelo de datos para las tareas.
│   ├── tests.py
│   ├── views.py           # Contiene las vistas que manejan la lógica de la aplicación.
│   ├── urls.py            # Configuración de URLs específicas para la aplicación de tareas.
│   └── templates/
│   │    └── tareas/
│   │        ├── index.html       # Plantilla para la vista principal de la aplicación.
│   │        └── edit_task.html   # Plantilla para la vista de edicion de tareas.
│   └── static/
│        └── main.css       # Archivo CSS principal para estilos del proyecto.
├── requirements.txt        # Lista de dependencias del proyecto.
└── README.md               # Documentación del proyecto.
```

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal del proyecto.
- **Django**: Framework web utilizado para el desarrollo de la aplicación.
- **PostgreSQL**: Sistema de gestión de base de datos relacional utilizado para almacenar y gestionar las tareas.
- **Bootstrap**: Framework front-end utilizado para el diseño y la interfaz de usuario del proyecto.
- **HTML y CSS**: Utilizados para la estructura y el estilo de las plantillas del proyecto.


Desarrollado por [Francisco](https://github.com/FrankSkep).
