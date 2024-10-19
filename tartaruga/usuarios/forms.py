from django import forms
from usuarios.models import Pessoa

fields = [
    'nome', 
    'idade', 
    'email',
    'telefone', 
    'dtNasc'
]

class UsuarioModelForm(forms.ModelForm):
    dtNasc = forms.DateField(
        input_formats = ['%d/%m/%Y'],
        label = 'Data do nascimento',
        help_text = 'Nascimento no formato DD/MM/AAAA',
    )
    class Meta:
        model = Pessoa
        fields = '__all__'
