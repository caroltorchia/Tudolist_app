
from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return  f"{self.nome}"

class Nota(models.Model):
    TIPO_CHOICES = [
        ('Exame', 'Exame'),
        ('Trabalho', 'Trabalho'),
    ]
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    nota = models.FloatField()
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    observacoes = models.TextField()

    REQUIRED_FIELDS = ["disciplina", "tipo", "nota"]

    def __str__(self):
        return f"{self.tipo} - {self.nota}"
