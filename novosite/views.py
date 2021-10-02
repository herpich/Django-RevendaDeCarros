from django.shortcuts import render, redirect
from novosite.forms import CarrosForm
from novosite.models import Carros

def home(request):
    dados = {}
    dados['db'] = Carros.objects.all()
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