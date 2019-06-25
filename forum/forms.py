from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset

from .models import Topico
from .models import Post
from .models import Coment

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

class ContatoForm(forms.Form):
    emissor = forms.EmailField(required=True, label='Remetente')
    assunto = forms.CharField(required=True)
    msg = forms.CharField(widget=forms.Textarea, label='Mensagem')

    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('emissor', css_class='form-group col-md-3 mx-auto'),
                Column('assunto', css_class='form-group col-md-3 mx-auto'),
                css_class='form-row'
            ),
            'msg'
        )
        self.helper.add_input(Submit('submit', 'Enviar', css_class='btn-success'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger '))

