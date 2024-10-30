# views.py
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NotaForm
from .models import Disciplina, Nota


def index(request):
    disciplinas = Disciplina.objects.filter(usuario=request.user)
    progresso = {}
    for disciplina in disciplinas:
        notas = Nota.objects.filter(disciplina=disciplina)
        media = sum(nota.nota for nota in notas) / len(notas) if notas else 0
        progresso[disciplina.nome] = {
            "notas": notas,
            "media": media,
            "alerta": media < 7.0,
        }
    return render(request, "index.html", {"progresso": progresso})

def visualizar_nota(request, nota_id=None):
    nota = get_object_or_404(Nota, id=nota_id)
    return render(request, "notas/visualizar.html", {"nota": nota})


def adicionar_nota(request):
    form = NotaForm()
    nota = Nota()

    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.usuario = request.user
            nota.save()
            return redirect("historico:index")

    return render(request, "notas/adicionar.html", {"form": form})

def editar_nota(request, nota_id=None):
    nota = get_object_or_404(Nota, id=nota_id)
    form = NotaForm(instance=nota)

    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.usuario = request.user
            nota.save()
            return redirect("historico:visualizar_nota", nota_id=nota.id)

    return render(request, "notas/editar.html", {"form": form, "nota": nota})

def revisar_nota(request, disciplina):
    messages.success(
        request, f"Review de nota da disciplina {disciplina} foi solicitado."
    )
    return redirect("historico:index")

def excluir_nota(request, nota_id=None):
    nota = get_object_or_404(Nota, id=nota_id)
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(nota)
    if nota.delete():
        messages.success(request, "Nota excluida com sucesso!")
    return redirect("historico:index")
