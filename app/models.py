from django.db import models


# Create your models here.
class VistaClientes(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    gerente = models.CharField(max_length=50)
    profesional= models.CharField(max_length=50)
    mail = models.EmailField()
    telefono = models.IntegerField()
    dirreccion = models.CharField(max_length=50)
    visitaprimaria = models.DateTimeField()
    visitasecundaria = models.DateTimeField()
    capacitacion = models.CharField(max_length=120)
    capacitacionfecha = models.DateTimeField()
    asesoria = models.CharField(max_length=50)
    asesoriafecha = models.DateTimeField()
    actividadmejora = models.CharField(max_length=120)
    accidentabilidad = models.IntegerField()
    def __str__(self):
        return self.rut 

class AsesoriaEspecial(models.Model) :
    razonsolicitud = models.CharField(max_length=50)
    fechasolicitud = models.DateField(null=True)
    asesoriafecha = models.DateField(null=True)
    descripcion = models.TextField()
    cliente = models.ForeignKey(VistaClientes, on_delete=models.PROTECT)
    def __str__(self):
        return self.razonsolicitud
