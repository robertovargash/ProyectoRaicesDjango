from pyexpat import model
from sys import maxsize
from unicodedata import decimal
from django.db import models
from django.forms import model_to_dict
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Clasificaciones(models.Model):
    clasificacion=models.CharField(max_length=30)
    detalles=models.CharField(max_length=1000)
    def __str__(self):
        return self.clasificacion #esto hace que donde quiera q yo diga objeto clasificacion me sale su nombre en vez de su id

    class Meta:
        # verbose_name = 'Clasificaciones'
        # verbose_name_plural = 'Clasificaciones'
        ordering = ['id']

class Almacen(models.Model):
    almacen=models.CharField(max_length=30, verbose_name='almacen',unique=True)
    descripcion=models.CharField(max_length=400)
    def __str__(self):
        return self.almacen

class Mercancia(models.Model):
    clasificacion = models.ForeignKey(Clasificaciones, on_delete=models.CASCADE)
    codigo=models.CharField(max_length=50)
    nombremercancia=models.CharField(max_length=1000)
    descripcion=models.CharField(max_length=1000)
    um=models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=18,decimal_places=6, default=0)   
    def __str__(self):
        return self.nombremercancia

class Almacenmercancia(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    mercancia = models.ForeignKey(Mercancia, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=18,decimal_places=6)    

class Recepcion(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    numero = models.IntegerField()
    observaciones = models.CharField(max_length=250,default="")
    precibe = models.CharField(max_length=250,default="")
    pentrega = models.CharField(max_length=250,default="")
    pautoriza = models.CharField(max_length=250,default="")
    contrato = models.CharField(max_length=50,default="")
    factura = models.CharField(max_length=50,default="")
    proveedor = models.CharField(max_length=250,default="")
    fecha = models.DateField()
    activo = models.IntegerField(default=0)

class Recepcionmercancias(models.Model):
    recepcion = models.ForeignKey(Recepcion, on_delete=models.CASCADE)
    mercancia = models.ForeignKey(Mercancia, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=18,decimal_places=6)
    precio = models.DecimalField(max_digits=18,decimal_places=6)

class Vale(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    numero = models.IntegerField()
    observaciones = models.CharField(max_length=250,default="")
    psolicita = models.CharField(max_length=250,default="")
    pentrega = models.CharField(max_length=250,default="")
    pautoriza = models.CharField(max_length=250,default="")
    fecha = models.DateField()
    activo = models.IntegerField(default=0)
    tipovale = models.IntegerField()
    
class Valeitems(models.Model):
    vale = models.ForeignKey(Vale, on_delete=models.CASCADE)
    mercancia = models.ForeignKey(Mercancia, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=18,decimal_places=6)
    precio = models.DecimalField(max_digits=18,decimal_places=6)