from django import forms

class FormularioContacto(forms.Form):

    asunto=forms.CharField(label="Nombre", required=True)
    email=forms.EmailField(label="Email", required=True)
    mensaje=forms.CharField(label="Contenido", widget=forms.Textarea)