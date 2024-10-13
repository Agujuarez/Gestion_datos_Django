from django.shortcuts import render, get_object_or_404
from .models import Autor, Libro
#from django.http import HttpResponse

# Create your views here.
def index_view(request):
    """Esto es la página principal"""

    autores = Autor.objects.all().order_by('id')

    return render(request, 'index.html', {'autores': autores})

def autor_view(request, id):
    """Esto es la página del autor"""
    autor = get_object_or_404(Autor, id=id)

    libros = Libro.objects.filter(autor=autor)

    return render(request, 'autor.html', {'autor': autor, 'libros': libros})