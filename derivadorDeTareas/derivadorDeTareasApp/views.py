from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Tarea, Comentario, Usuario
from django.http import HttpResponseForbidden
from .forms import TareaForm, ComentarioForm, UsuarioForm, RegistroUsuarioForm, CambiarContrasenaForm, GestionUsuarioForm

def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('menu_admin')
            else:
                return redirect('menu_usuario')
        else:
            return render(request, 'index.html', {'error': 'Credenciales inválidas'})
    return render(request, 'index.html')

@login_required
def menu_admin(request):
    return render(request, 'menu_admin.html')

@login_required
def menu_usuario(request):
    return render(request, 'menu_usuario.html')

@login_required
def lista_tareas(request):
    query = request.GET.get('q')
    if query:
        tareas = Tarea.objects.filter(nombre__icontains=query)
    else:
        tareas = Tarea.objects.all()

    for tarea in tareas:
        tarea.ultimo_comentario = tarea.comentarios.last()
    
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.tarea = tarea
            comentario.usuario = request.user
            comentario.save()
            return redirect('detalle_tarea', pk=tarea.pk)
    else:
        form = ComentarioForm()
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea, 'form': form})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.asignada_por = request.user
            tarea.save()
            messages.success(request, 'Se generó el registro.')
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/crear_tarea.html', {'form': form})

@login_required
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    comentarios = tarea.comentarios.all()
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        comentario_form = ComentarioForm(request.POST)
        if form.is_valid() and comentario_form.is_valid():
            form.save()
            comentario = comentario_form.save(commit=False)
            comentario.tarea = tarea
            comentario.usuario = request.user
            comentario.save()
            messages.success(request, 'Se actualizó el registro y se agregó el comentario.')
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
        comentario_form = ComentarioForm()
    return render(request, 'tareas/editar_tarea.html', {'form': form, 'comentario_form': comentario_form, 'comentarios': comentarios})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, 'Tarea eliminada.')
        return redirect('lista_tareas')
    return render(request, 'tareas/eliminar_tarea.html', {'tarea': tarea})

@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def detalle_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuarios/detalle_usuario.html', {'usuario': usuario})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def crear_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('lista_usuarios')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado.')
        return redirect('lista_usuarios')
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('inicio')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def gestionar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = GestionUsuarioForm(request.POST, request.FILES, instance=usuario)
        password_form = CambiarContrasenaForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            if password_form.is_valid():
                password_form.save()
            return redirect('menu_usuario')
    else:
        form = GestionUsuarioForm(instance=usuario)
        password_form = CambiarContrasenaForm(user=request.user)
    return render(request, 'usuarios/gestionar_usuario.html', {'form': form, 'password_form': password_form})

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = CambiarContrasenaForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('cambiar_contrasena_done')
    else:
        form = CambiarContrasenaForm(user=request.user)
    return render(request, 'usuarios/cambiar_contrasena.html', {'form': form})

@login_required
def cambiar_contrasena_done(request):
    return render(request, 'usuarios/cambiar_contrasena_done.html')

def logout_view(request):
    logout(request)
    return redirect('inicio')

def acerca_de(request):
    return render(request, 'acerca_de.html')
