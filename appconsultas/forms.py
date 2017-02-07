from django.forms import ModelForm, forms
from django import forms
from appconsultas.models import *

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields=('nome','crm','especialidade')

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields=('nome','cpf','endereco','telefone','dataNascimento')

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields=('medico','paciente','horario')

