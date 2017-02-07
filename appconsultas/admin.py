from django.contrib import admin

# Register your models here.
from appconsultas.models import *

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)