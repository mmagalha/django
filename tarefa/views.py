from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm
from django.shortcuts import render, get_object_or_404


def lista_tarefa(request):
    tarefas = Tarefa.objects.filter().order_by('prioridade')
    return render(request, 'lista_tarefa.html', {'tarefas': tarefas})

def tarefa_detail(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'tarefa_detail.html', {'tarefa': tarefa})

def tarefa_new(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.save()
#            return redirect('/',)
    else:
        form = TarefaForm()
    return render(request, 'tarefa_edit.html', {'form': form})


def tarefa_edit(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == "POST":
        form = TarefaForm(request.POST, instance=Tarefa)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.created_date = timezone.now()
            tarefa.save()
            return redirect('tarefa_detail', pk=post.pk)
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefa_edit.html', {'form': form})