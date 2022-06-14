from django.http import HttpResponse
from django.shortcuts import render

from .models import Student

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def show_students(request):
    lista_studenti = Student.objects.all()
    studenti = "<br/>".join(s.nume for s in lista_studenti)
    return HttpResponse(studenti)