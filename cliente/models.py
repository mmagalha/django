from django.db import models
from django.utils import timezone
# Create your models here.

class Cliente(models.Model):
    criado_por = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)