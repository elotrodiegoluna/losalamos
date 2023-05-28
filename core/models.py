from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.db import models
# Create your models here.




class TipoUsuario(models.Model):
    idTipoUsuario = models.IntegerField(primary_key="true")
    tipoUsuario = models.CharField(max_length=20)

class Usuario(AbstractUser):
    # CUSTOM
    nombre = models.CharField(max_length=45, default='nombre')
    rut = models.CharField(max_length=45, default='123')
    fecha_nacimiento = models.DateField(null=True)
    nro_telefono = models.IntegerField(default=123132)
    tipoUsuario_idTipoUsuario = models.ForeignKey(
        TipoUsuario,
        on_delete=models.CASCADE,
        db_column='especialidad_idEspecialidad',)
    # DEFAULT
    username = None
    email = models.EmailField(_("email address"), unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['nombre', 'rut']

    
    def __str__(self):
        return self.email


    class Meta:
        db_table = 'tipoUsuario'


class Especialidad(models.Model):
    nombreEspecialidad = models.CharField(max_length=45)
    class Meta:
        db_table = 'especialidad'


class Medico(models.Model):
    nombre = models.CharField(max_length=45)
    especialidad_idEspecialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.CASCADE,
        db_column='especialidad_idEspecialidad',
    )
    idMedico = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'medico'


class Venta(models.Model):
    precio = models.CharField(max_length=45)
    fechaVenta = models.DateField()
    idVenta = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'venta'


class TipoServicio(models.Model):
    idtipoServicio = models.IntegerField(primary_key=True)
    nombreServicio = models.CharField(max_length=45)
    medico_idMedico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        db_column='medico_idMedico',
    )

    class Meta:
        db_table = 'tipoServicio'


class Servicio(models.Model):
    idservicio = models.IntegerField(primary_key=True)
    nombreServicio = models.CharField(max_length=45)
    tipoServicio_idtipoServicio = models.ForeignKey(
        TipoServicio,
        on_delete=models.CASCADE,
        db_column='tipoServicio_idtipoServicio',
    )

    class Meta:
        db_table = 'servicio'




class ReservaHora(models.Model):
    fecha = models.CharField(max_length=45)
    hora = models.CharField(max_length=50)
    medico_idMedico = models.ForeignKey(
    
        Medico,
        on_delete=models.CASCADE,
        db_column='medico_idMedico',
    )
    venta_idVenta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        db_column='venta_idVenta',
    )
    servicio_idservicio = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE,
        db_column='servicio_idservicio',
    )
    usuario_idusuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='paciente_idUsuarios',
    )
    idreservaHora = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'reservaHora'

    

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Paciente(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, default='nombre')
    rut = models.CharField(max_length=45, default='123')
    fecha_nacimiento = models.DateField(null=True)
    nro_telefono = models.IntegerField(default=123132)
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.nombre