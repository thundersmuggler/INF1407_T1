from django.shortcuts import render

# Create your views here.

from usuarios.models import Pessoa
from django.views.generic.base import View

class UsuarioListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = { 'pessoas': pessoas, }
        return render(request, 'usuarios/listaUsuarios.html', contexto)

class CadastrarUsuarioView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = { 'pessoas': pessoas, }
        return render(request, 'usuarios/listaUsuarios.html', contexto)