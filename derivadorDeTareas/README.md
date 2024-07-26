# Gestión de Tareas

## Descripción General
La aplicación "Gestión de Tareas" es una herramienta web colaborativa desarrollada con Django que permite a los usuarios gestionar proyectos y tareas de manera eficiente. Incluye funcionalidades de autenticación, gestión de usuarios, tareas y comentarios, y permisos específicos para administradores y usuarios normales.

## Tecnologías Utilizadas
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap)
- **Base de Datos:** SQLite
- **Autenticación y Autorización:** Django Authentication System

## Funcionalidades Principales

### Autenticación de Usuarios
- Registro de nuevos usuarios.
- Inicio y cierre de sesión.
- Los administradores pueden gestionar todos los usuarios y sus tareas.

### Gestión de Usuarios
- Los administradores pueden ver, crear, editar y eliminar usuarios.
- Los usuarios pueden editar su propio perfil y cambiar su contraseña.

### Gestión de Tareas
- Crear, ver, editar y eliminar tareas.
- Listado de tareas con detalles como nombre, fechas, urgencia, tarea anterior, asignada por y el último mensaje.
- Búsqueda de tareas por nombre.
- Asignar tareas a otros usuarios.
- Agregar comentarios a las tareas con registro de fecha y hora.

### Interfaz de Usuario
- Interfaz limpia y responsiva basada en Bootstrap.
- Formularios estilizados para facilitar la entrada de datos.
- Mensajes de éxito y error proporcionan retroalimentación a los usuarios.

### Seguridad y Permisos
- Decoradores de vista aseguran que solo los usuarios autenticados puedan acceder a ciertas vistas.
- Los administradores tienen permisos adicionales para gestionar usuarios y tareas.

### Páginas Específicas
- **Inicio de Sesión:** Permite a los usuarios iniciar sesión.
- **Menú de Usuario:** Acceso a la lista de tareas y gestión del perfil.
- **Menú de Administrador:** Gestión de usuarios y visualización de todas las tareas.
- **Lista de Tareas:** Muestra todas las tareas en una tabla con opciones para editar y eliminar.
- **Detalle de Tarea:** Muestra los detalles de una tarea específica y los comentarios asociados.
- **Crear/Editar Tarea:** Formularios para crear y editar tareas.
- **Lista de Usuarios:** Muestra todos los usuarios en una tabla con opciones para editar y eliminar.
- **Crear/Editar Usuario:** Formularios para crear y editar usuarios.
- **Gestionar Usuario:** Permite a los usuarios editar su perfil y cambiar su contraseña.
- **Acerca de:** Información sobre el desarrollador.

## Instalación y Configuración

### Requisitos Previos
- Python 3.x
- Django
- SQLite (o cualquier otro motor de base de datos compatible con Django)


## Uso de la Aplicación

### Registro e Inicio de Sesión
1. **Registro:**
    - Navega a la página de registro (`/registro/`) y completa el formulario de registro.
2. **Inicio de Sesión:**
    - Navega a la página de inicio de sesión (`/`) y completa el formulario con tus credenciales.

### Gestión de Usuarios
- Los administradores pueden acceder al menú de administración para gestionar usuarios (`/menu_admin/`).

### Gestión de Tareas
- Los usuarios pueden crear, ver, editar y eliminar tareas desde su menú principal (`/menu_usuario/`).

### Comentarios en Tareas
- Los usuarios pueden agregar comentarios a las tareas al editar una tarea específica.

### Usuarios de prueba generados


- **Nombre**:Fernando Chiesa
- **Usuario**:infocctv.ef@gmail.com
- **Contraseña**:milanesa
- **Avatar**:avatar 1

- **Nombre**:Valeria bera
- **Usuario**: lavale@gmail.com
- **Contraseña**:napolitana-> cambio a -> milanesazuiza
- **Avatar**:avatar 3

- **Nombre**:Mario correa
- **Usuario**:Mariocorrea@gmail.com
- **Contraseña**:olgaolga


- **Nombre**:Damian Rossi 
- **Usuario**:damianrossi@gmail.com
- **Contraseña**:elsantafesino

- **Nombre**:migue rio
- **Contraseña**:santander@gmail.com
- **Contraseña**:quebanco

### Video Link
- **Video**: https://drive.google.com/file/d/1NfQna9y0zpPCiHfDyHr5bIXDuaeLVvVI/view?usp=drive_link