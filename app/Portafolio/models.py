from django.db import models

class Usuario(models.Model):
    codigo_usurio = models.IntegerField(max_length=25,null=False,unique=True,primary_key=True)
    primer_nombre = models.CharField(max_length=25,null=False)
    segundo_nombre = models.CharField(max_length=25,null=True)
    primer_apellido = models.CharField(max_length=25,null=False)
    segundo_apellido = models.CharField(max_length=25,null=True)
    numero_celular = models.IntegerField(max_length=25,null=False)
    correo_electronico = models.EmailField(max_length=100,null=False)
    url_git = models.TextField()

class Proyectos(models.Model):
    id  = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=100,null=False)
    descripcion_proyecto = models.TextField()
    url_git_proyecto = models.TextField()
    url_pag_proyecto = models.TextField()
    nombre_img = models.TextField()