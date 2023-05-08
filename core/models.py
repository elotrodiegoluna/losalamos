from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=45)
    constraseña = models.CharField(max_length=45)
    rut = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    correo = models.CharField(max_length=45)
    nro_telefono = models.IntegerField()

    class Meta:
        db_table = 'paciente'


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
    paciente_idUsuarios = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        db_column='paciente_idUsuarios',
    )
    idreservaHora = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'reservaHora'

    from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title