# views.py
from django.shortcuts import render, redirect
from .models import Disciplina, Nota
from .forms import NotaForm
from django.contrib import messages

def index(request):
    disciplinas = Disciplina.objects.filter(usuario=request.user)
    progresso = {}
    for disciplina in disciplinas:
        notas = Nota.objects.filter(disciplina=disciplina)
        media = sum(nota.nota for nota in notas) / len(notas) if notas else 0
        progresso[disciplina.nome] = {
            'notas': notas,
            'media': media,
            'alerta': media < 7.0
        }
    return render(request, 'index.html', {'progresso': progresso})

def adicionar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historico:index')
    else:
        form = NotaForm()
    return render(request, 'adicionar.html', {'form': form})

def revisar_nota(request, disciplina):
    messages.success(request, f'Review de nota da disciplina {disciplina} foi solicitado.')
    return redirect('historico:index')
