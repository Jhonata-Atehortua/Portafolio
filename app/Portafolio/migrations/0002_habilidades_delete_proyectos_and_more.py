# Generated by Django 4.2.4 on 2023-10-11 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Proyectos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='codigo_usurio',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='correo_electronico',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='numero_celular',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='primer_apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='primer_nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='segundo_apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='segundo_nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='url_git',
        ),
        migrations.AddField(
            model_name='usuario',
            name='Codigo',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Correo',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='PrimerApellido',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='PrimerNombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Url_Instagram',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='habilidades',
            name='CodigoU',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Portafolio.usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Url_Git',
            field=models.TextField(null=True),
        ),
    ]
