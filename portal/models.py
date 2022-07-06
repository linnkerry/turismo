from __future__ import unicode_literals
from audioop import max
from django.db import models
from django.contrib.gis.db import models

class TypePerson(models.Model):
    descripcion = models.CharField(max_length=50)
    objects = models.Manager()
    def __str__(self):
        return self.descripcion

class Radio(models.Model):
    descripcion = models.CharField(max_length=10)
    ubicacion = models.PointField(srid=4326)
    def __str__(self):
        return self.descripcion

class Person(models.Model):
    SEXO_CHOICES = [
        ('1','MASCULINO'),
        ('2','FEMENINO'),
    ]
    nombre = models.CharField(max_length=50)
    apepaterno = models.CharField(max_length=50)
    apematerno = models.CharField(max_length=50)
    documento = models.CharField(max_length=8)
    sexo = models.CharField(max_length=1,choices=SEXO_CHOICES)
    fecnacimiento = models.DateField(null=True, blank=True)
    celular = models.CharField(max_length=15,null=True, blank=True)
    direccion = models.CharField(max_length=150, null=True, blank=True)
    radio = models.ForeignKey(Radio,null=True, blank=True, on_delete=models.SET_NULL)
    typeperson = models.ForeignKey(TypePerson, null=True,blank=True,on_delete=models.SET_NULL)
    objects = models.Manager()
    def __str__(self):
        return self.nombre + ' ' + self.apepaterno +' '+ self.apematerno

# Create your models here.
class TypeIncidence(models.Model):
    descripcion = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=50, null=True,blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name_plural = "Type Incidence"

class Vehiculo(models.Model):
    VEHICULO_CHOICE = [
        ('1','CAMIONETA'),
        ('2','MOTOCICLETA'),
    ]
    ASIGNADO_CHOICE = [
        ('1','ASIGNADO'),
        ('2','NO ASIGNADO'),
    ]
    modelo = models.CharField(max_length=1,null=True,blank=True,choices=VEHICULO_CHOICE)
    placa = models.CharField(max_length=10,null=True,blank=True)
    asignado = models.CharField(max_length=1, null=True, blank=True, choices=ASIGNADO_CHOICE)
    def __str__(self):
        return self.placa

class Incidences(models.Model):
    location = models.PointField(srid=4326)
    objects = models.Manager()
    fecincidencia = models.DateTimeField(auto_now=True)
    fecactuainsidencia = models.DateTimeField(auto_now_add=True)
    agente = models.ForeignKey(Person, related_name="agente",on_delete=models.SET_NULL, null=True,blank=True)
    agraviado = models.ForeignKey(Person, related_name="agraviado",on_delete=models.SET_NULL, null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL,null=True,blank=True)
    typeinsidence = models.ForeignKey(TypeIncidence, on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.typeinsidence.descripcion
    def natural_key(self):
        return self.typeinsidence.natural_key()
    natural_key.dependencies = ['portal.typeincidence']
    class Meta:
        verbose_name_plural = "Incidences"
