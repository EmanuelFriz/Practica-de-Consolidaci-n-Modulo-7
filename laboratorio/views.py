from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Laboratorio
from .forms import LaboratorioForm



def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio_list.html', {'laboratorios': laboratorios})

@login_required
def laboratorio_detail(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    return render(request, 'laboratorio_detail.html', {'laboratorio': laboratorio})

@login_required
def laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio_form.html', {'form': form})

@login_required
def laboratorio_update(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio_form.html', {'form': form})

@login_required
def laboratorio_delete(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio_list')
    return render(request, 'laboratorio_confirm_delete.html', {'laboratorio': laboratorio})
