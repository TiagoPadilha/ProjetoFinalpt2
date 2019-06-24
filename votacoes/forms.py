from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Time
from .models import Escolha

class FormTime(forms.ModelForm):

    class Meta:
        model = Time
        fields = ('time', )
        

class FormEscolha(forms.ModelForm):

    class Meta:
        model = Escolha
        fields = ('Equipe_da_casa', 'votes', 'Equipe_de_fora','votes2','Partida')



