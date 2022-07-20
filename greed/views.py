from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request,'formCadastroHorario.html')
  