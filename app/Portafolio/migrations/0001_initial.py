# Generated by Django 4.2.4 on 2023-08-27 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proyecto', models.CharField(max_length=100)),
                ('descripcion_proyecto', models.TextField()),
                ('url_git_proyecto', models.TextField()),
                ('url_pag_proyecto', models.TextField()),
                ('nombre_img', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo_usurio', models.IntegerField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('primer_nombre', models.CharField(max_length=25)),
                ('segundo_nombre', models.CharField(max_length=25, null=True)),
                ('primer_apellido', models.CharField(max_length=25)),
                ('segundo_apellido', models.CharField(max_length=25, null=True)),
                ('numero_celular', models.IntegerField(max_length=25)),
                ('correo_electronico', models.EmailField(max_length=100)),
                ('url_git', models.TextField()),
            ],
        ),
    ]