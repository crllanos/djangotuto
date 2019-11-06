from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(req):
    return HttpResponse('<title>tutorial Django</title>Hola poh <b>machucao</b> # req: ' + str(req))
