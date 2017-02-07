from django.db import models

# Create your models here.
class Medico(models.Model):
    nome = models.CharField("Nome do Medico", max_length=150)
    crm = models.CharField("CRM", max_length=20)
    especialidade = models.CharField("Especialidade", max_length=255)

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome = models.CharField("Nome do Paciente", max_length=150)
    cpf = models.CharField("CPF", max_length=15)
    endereco = models.CharField("Endereço", max_length=500)
    telefone = models.CharField("Telefone", max_length=11)
    dataNascimento = models.DateField("Data de Nascimento")

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, verbose_name="Medico")
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Paciente")
    horario = models.CharField("Horário da consulta", max_length=20)



