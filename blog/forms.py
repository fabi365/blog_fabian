from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'categoria', 'autor']

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if not titulo:
            raise forms.ValidationError("Este campo es obligatorio.")
        return titulo
