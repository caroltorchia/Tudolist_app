# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notas/<int:id>/edit", views.adicionar_nota, name="editar_nota"),
    path('notas/add', views.adicionar_nota, name='adicionar_nota'),
    path('revisar_nota/<str:disciplina>/', views.revisar_nota, name='revisar_nota'),
]
