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

def adicionar_nota(request, id=None):
    if id:
        nota = Nota.objects.get(id=id)
        form = NotaForm(instance=nota)
    else:
        form = NotaForm()

    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.usuario = request.user
            nota.save()
            return redirect('historico:index')

    return render(request, 'adicionar.html', {'form': form})

def revisar_nota(request, disciplina):
    messages.success(request, f'Review de nota da disciplina {disciplina} foi solicitado.')
    return redirect('historico:index')
