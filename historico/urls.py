# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('notas/add', views.adicionar_nota, name='adicionar_nota'),
    path("notas/<int:nota_id>/edit", views.editar_nota, name="editar_nota"),
    path('notas/<int:nota_id>', views.visualizar_nota, name='visualizar_nota'),
    path('notas/<int:nota_id>/delete', views.excluir_nota, name='excluir_nota'),
]
