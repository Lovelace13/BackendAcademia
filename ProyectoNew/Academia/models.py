# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aula(models.Model):
    idaula = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=60)
    tema = models.CharField(max_length=60, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    idasignatura = models.IntegerField(blank=True, null=True)
    ideducador = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='ideducador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aula'

class Materia(models.Model):
    idmateria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materia'

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    idprofesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    cedula = models.CharField(max_length=10, blank=True, null=True)
    idasignatura = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesor'
