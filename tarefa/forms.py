from django import forms

from .models import Tarefa

class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ('nome', 'descricao','inicio', 'fim', 'prioridade', 'responsavel')