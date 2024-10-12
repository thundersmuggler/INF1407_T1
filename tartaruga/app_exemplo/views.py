from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home(request):
	# return HttpResponse('alô alô graças a deus')
	return render(request, 'app_exemplo/home.html')

def segunda_pagina(request):
	return render(request, 'app_exemplo/segunda.html')