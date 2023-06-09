# Generated by Django 4.2.1 on 2023-05-19 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nombre', models.CharField(default='nombre', max_length=45)),
                ('rut', models.CharField(default='123', max_length=45)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('nro_telefono', models.IntegerField(default=123132)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEspecialidad', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'especialidad',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('nombre', models.CharField(max_length=45)),
                ('idMedico', models.IntegerField(primary_key=True, serialize=False)),
                ('especialidad_idEspecialidad', models.ForeignKey(db_column='especialidad_idEspecialidad', on_delete=django.db.models.deletion.CASCADE, to='core.especialidad')),
            ],
            options={
                'db_table': 'medico',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('precio', models.CharField(max_length=45)),
                ('fechaVenta', models.DateField()),
                ('idVenta', models.IntegerField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(null=True)),
            ],
            options={
                'db_table': 'venta',
            },
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('idtipoServicio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreServicio', models.CharField(max_length=45)),
                ('medico_idMedico', models.ForeignKey(db_column='medico_idMedico', on_delete=django.db.models.deletion.CASCADE, to='core.medico')),
            ],
            options={
                'db_table': 'tipoServicio',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idservicio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreServicio', models.CharField(max_length=45)),
                ('tipoServicio_idtipoServicio', models.ForeignKey(db_column='tipoServicio_idtipoServicio', on_delete=django.db.models.deletion.CASCADE, to='core.tiposervicio')),
            ],
            options={
                'db_table': 'servicio',
            },
        ),
        migrations.CreateModel(
            name='ReservaHora',
            fields=[
                ('fecha', models.CharField(max_length=45)),
                ('hora', models.CharField(max_length=50, null=True)),
                ('idreservaHora', models.IntegerField(primary_key=True, serialize=False)),
                ('medico_idMedico', models.ForeignKey(db_column='medico_idMedico', on_delete=django.db.models.deletion.CASCADE, to='core.medico')),
                ('paciente_idUsuarios', models.ForeignKey(db_column='paciente_idUsuarios', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('servicio_idservicio', models.ForeignKey(db_column='servicio_idservicio', on_delete=django.db.models.deletion.CASCADE, to='core.servicio')),
                ('venta_idVenta', models.ForeignKey(db_column='venta_idVenta', on_delete=django.db.models.deletion.CASCADE, to='core.venta')),
            ],
            options={
                'db_table': 'reservaHora',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('description', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
