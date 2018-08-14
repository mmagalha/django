from django.db import models
from django.db.models import IntegerField
from django.utils import timezone
from projeto.models import Projeto
# Create your models here.

class Tarefa(models.Model):
    responsavel = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    inicio = models.DateTimeField(blank=True, null=True)
    fim = models.DateTimeField(blank=True, null=True)
    prioridade = IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    projeto = models.ForeignKey(Projeto, related_name='tarefas', on_delete=models.CASCADE)

    def __str__(self):
       return self.nome