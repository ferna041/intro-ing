from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('description','grado',"asignatura_Media","asignatura_Basica","image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({"class": "form-control"})