# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('adicionar_nota/', views.adicionar_nota, name='adicionar_nota'),
    path('revisar_nota/<str:disciplina>/', views.revisar_nota, name='revisar_nota'),
]
