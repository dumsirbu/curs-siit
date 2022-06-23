from django.http import HttpResponse
from django.shortcuts import render

from .models import Student

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def show_students(request):
    try:
        an_cerut = int(request.GET['an'])
        lista_studenti = Student.objects.filter(an=an_cerut)
    except KeyError:
        lista_studenti = Student.objects.all()

    context = {
        'studenti': lista_studenti,
        'mesaj': 'Salut'
    }
    return render(request, "list_students.html", context)