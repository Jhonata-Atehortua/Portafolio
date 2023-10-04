from django import forms

class Contactanos(forms.Form):
    nombre=forms.CharField(required=True,label="Nombres Completos")
    correo = forms.CharField(required=True,label="Correo Electronico")
    telefono = forms.IntegerField(required=True,label="Numero Celular")
    