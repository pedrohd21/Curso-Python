from django.db import models
from contatos.models import Contato  # importar Contato de contato/views
from django import forms    #importa os formularios que vai ser utilizado no dashboard


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato         # representar os campos contato
        exclude = ('mostrar',)

