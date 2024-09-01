from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.db.models import Q

def lista_publicaciones(request):
    #agrege esta linea de codigo que no tenia.
    query = request.GET.get('q')
    fecha = request.GET.get('fecha')
    categoria = request.GET.get('categoria')

    queryset = Post.objects.all()
    # Filtrado por fecha y categoría
    fecha = request.GET.get('fecha_publicacion')
    categoria = request.GET.get('categoria')
    if fecha:
        queryset = queryset.filter(fecha_publicacion=fecha)
    if categoria:
        queryset = queryset.filter(categoria__icontains=categoria)

    # Búsqueda por título o contenido
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(titulo__icontains=query) |
            Q(contenido__icontains=query)
        )

    paginator = Paginator(queryset, 10)  # 10 publicaciones por página
    page = request.GET.get('page')
    publicaciones = paginator.get_page(page)

    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion})

def agregar_publicacion(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PostForm()
    return render(request, 'blog/agregar_publicacion.html', {'form': form})

def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('detalle_publicacion', pk=pk)
    else:
        form = PostForm(instance=publicacion)
    return render(request, 'blog/editar_publicacion.html', {'form': form})


