from django.shortcuts import render

# Create your views here.

from usuarios.models import Pessoa
from django.views.generic.base import View


from usuarios.forms import UsuarioModelForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy


class UsuarioListView(View):
    
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = { 'pessoas': pessoas, }
        return render(request, 'usuarios/listaUsuarios.html', contexto)


class CadastrarUsuarioView(View):

    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': UsuarioModelForm, }
        return render(request, "usuarios/cadastrar_usuario.html", contexto)
    
    def post(self, request, *args, **kwargs):
        formulario = UsuarioModelForm(request.POST)
        if formulario.is_valid():
            contato = formulario.save()
            contato.save()
            return HttpResponseRedirect(reverse_lazy("usuarios:lista-usuarios"))
