from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.
from appconsultas.forms import *
@login_required(login_url='login')
def home(request):
    return render(request, 'base.html')

@login_required(login_url='login')
def medico_new(request):
    if(request.method=='POST'):
        form=MedicoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('medico_list')
    else:
        form=MedicoForm()
    dados={'form':form}
    return render(request,'medicos/medico_form.html',dados)

@login_required(login_url='login')
def medico_list(request):
    medicos = Medico.objects.all().order_by('nome')
    dados = {'medicos': medicos}
    return render(request, 'medicos/medico_list.html', dados)

@login_required(login_url='login')
def paciente_new(request):
    if(request.method=='POST'):
        form=PacienteForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('paciente_list')
    else:
        form=PacienteForm()
    dados={'form':form}
    return render(request,'pacientes/paciente_form.html',dados)

@login_required(login_url='login')
def paciente_list(request):
    pacientes = Paciente.objects.all().order_by('nome')
    dados = {'pacientes': pacientes}
    return render(request, 'pacientes/paciente_list.html', dados)

@login_required(login_url='login')
def consulta_new(request):
    if(request.method=='POST'):
        form=ConsultaForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('consulta_list')
    else:
        form=ConsultaForm()
    dados={'form':form}
    return render(request,'consultas/consulta_form.html',dados)

@login_required(login_url='login')
def consulta_list(request):
    consultas = Consulta.objects.all()
    dados = {'consultas': consultas}
    return render(request, 'consultas/consulta_list.html', dados)

#FIM NADA
