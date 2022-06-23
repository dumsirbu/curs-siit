from django.http import HttpResponse
from django.shortcuts import render

from .models import Student

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")


def show_students(request):
    try:
        an_cerut = int(request.GET['an'])
        nume = request.GET['nume']
        lista_studenti = Student.objects.filter(an__lte=an_cerut, nume__startswith=nume)
    except KeyError:
        lista_studenti = Student.objects.all()
    context = {
        'studenti': lista_studenti,
        'mesaj': 'Salut'
    }
    return render(request, "list_students.html", context)


def filter(*args, **kwargs):
    pass