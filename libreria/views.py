from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    # print(f'descripcion de libros: ${libros}')
    return render(request, 'libros/index.html',{'libros': libros  })


def crear_libro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if(formulario.is_valid()):
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html',{'formulario': formulario  })

def editar(request,id):
    libro=Libro.objects.get(id=id) # se octiene la consulta del libro
    formulario=LibroForm(request.POST or None, request.FILES or None, instance=libro)# se le pasa la consulta del libro y el formulario
    if(formulario.is_valid()) and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html',{'formulario': formulario })


def eliminar(request, id_libro):
    libro=Libro.objects.get(id=id_libro)
    libro.delete()
    return redirect('libros')



