from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)
    estilo = models.CharField(max_length=30)
    ibu = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    marca = models.CharField(max_length=50)
    porcentaje_alcohol = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    precio_regular = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)])
    precio_happy_hour = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)])
    volumen = models.CharField(max_length=20)
    imagen = models.URLField(default='', blank=True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - marca: {self.marca} - estilo: {self.estilo} - Precio regular: {self.precio_regular} - Precio Happy Hour: {self.precio_happy_hour}" 
    
class Comida(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio_regular = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)])
    precio_happy_hour = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)])
    foto = models.URLField(default='', blank=True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Descripción: {self.descripcion}"
    
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha = models.DateField()
    horario = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Descripción: {self.descripcion} - Fecha: {self.fecha} - Horario: {self.horario}"

class Promo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    horario = models.CharField(max_length=100)
    
    def __str__(self):
        txt="{0} - {1}"
        return f"Nombre: {self.nombre} - Descripción: {self.descripcion} - Precio: {self.precio} - Horario: {self.horario}"
    
class Valoracion(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    imagen = models.URLField(default='', blank=True)
    email = models.EmailField()
    opinion = models.CharField(max_length=500)
    fecha = models.DateField()
    estrellas = models.IntegerField(default=0)
    
    def __str__(self):
        txt="{0},{1} - {2} - {3} - {4} "
        return txt.format(self.nombre, self.apellido, self.imagen, self.opinion, self.estrellas)
    
    class Meta:
        verbose_name="Valoraciones"
        verbose_name_plural = "Valoraciones"
        
"""
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null = True, blank = True)
"""    