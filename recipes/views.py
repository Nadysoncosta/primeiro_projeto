from django.http import HttpResponse

# from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('HOME estou aprendendo 4')


def contato(request):
    return HttpResponse('CONTATO')


def sobre(request):
    return HttpResponse('SOBRE')
