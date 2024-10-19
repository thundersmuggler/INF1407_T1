from django.db import models

# Create your models here.
class Pessoa(models.Model):

    id = models.AutoField(primary_key=True)
    
    nome = models.CharField(
        max_length = 100, 
        help_text = 'Nome do usuário')
    
    idade = models.IntegerField(
        help_text = 'Idade do usuário')
    
    email = models.EmailField(
        help_text='E-Mail do usuário', 
        max_length = 254)
    
    telefone = models.CharField(
        help_text='Telefone do usuário', 
        max_length = 20)
    
    dtNasc = models.DateField(
        help_text='Data de nascimento do usuário',
        verbose_name='Data de nascimento')

    def __str__(self):
        return self.nome
