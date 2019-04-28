from django import forms

from .models import Topico
from .models import Post
from.models import Coment

class FormTopico(forms.ModelForm):

    class Meta:
        model = Topico
        fields = ('titulo', 'descricao', )

class FormPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'topico', 'body')

class FormComent(forms.ModelForm):

    class Meta:
        model = Coment
        fields = ('body','post',)

