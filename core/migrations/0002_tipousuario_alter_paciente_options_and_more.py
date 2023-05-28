# Generated by Django 4.0.4 on 2023-05-28 20:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('idTipoUsuario', models.IntegerField(primary_key='true', serialize=False)),
                ('tipoUsuario', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='paciente',
            options={},
        ),
        migrations.RenameField(
            model_name='reservahora',
            old_name='paciente_idUsuarios',
            new_name='usuario_idusuario',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='password',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='user_permissions',
        ),
        migrations.CreateModel(
            name='Usuario',
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
                ('tipoUsuario_idTipoUsuario', models.ForeignKey(db_column='especialidad_idEspecialidad', on_delete=django.db.models.deletion.CASCADE, to='core.tipousuario')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'tipoUsuario',
            },
        ),
    ]
