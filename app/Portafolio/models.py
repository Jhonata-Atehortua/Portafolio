from django.db import models

class Usuario(models.Model):
    Codigo = models.IntegerField(primary_key=True,default=0)
    PrimerNombre = models.CharField(max_length=100,null=True)
    PrimerApellido = models.CharField(max_length=100,null=True)
    Correo = models.EmailField(max_length=100,null=True)
    Url_Git = models.TextField(null=True)
    Url_Instagram = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.PrimerNombre} {self.PrimerApellido}"
    
    def ObtenerInfoUsuario():
        Info = Usuario.objects.all()
        return Info

class Habilidades(models.Model):
    id = models.AutoField(primary_key=True)
    CodigoU = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
    Nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Nombre
    
    def ObtenerHabilidadesUsuario():
        Info = Habilidades.objects.all()
        return Info