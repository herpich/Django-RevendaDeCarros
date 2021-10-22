from django.shortcuts import render, redirect
from novosite.forms import CarrosForm
from novosite.models import Carros
from django.core.paginator import Paginator

def home(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        dados['db'] = Carros.objects.all()

    #all = Carros.objects.all()
    #paginator = Paginator(all, 4)
    #pages = request.GET.get('page')
    #dados['db'] = paginator.get_page(pages)
    return render(request, 'index.html', dados)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html',data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')