from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Student, Curs
from .forms import LoginForm

# Create your views here.
def hello_world(request):
    def my_func():
        return "salutare"

    class MyObject:
        proprietate = 1

        def __init__(self, id):
            self.id = id

    obj = MyObject(10)

    context = {
        'time': timezone.now(),
        'string': "Salut",
        'lista': [1,2,3],
        'dictionar': {
            'unu': 1,
            'doi': 2,
            'dict2': {
                'cheie': 'valoare'
            },
        
        },
        'functie': my_func,
        'obiect': obj,
        #'cheie': 'Valoare'
    }
    return render(request, "homepage.html", context)


def show_students(request):
    try:
        an_cerut = int(request.GET['an'])
        lista_studenti = Student.objects.filter(an__lte=an_cerut,)
    except KeyError:
        lista_studenti = Student.objects.all()

    try:
        nume = request.GET['nume']
        lista_studenti = lista_studenti.filter(nume__startswith=nume)
    except KeyError:
        pass
    
    promoveaza = request.GET.get("promoveaza")
    if promoveaza is not None:
        lista_studenti.update(an=2)
        # Student.objects.update(an=2) - va modifica toate intrarile din DB
    sterge = request.GET.get("sterge")
    if sterge is not None:
        print(sterge)
        lista_studenti.delete()
        #  Student.objects.delete() - va sterge toate intrarile
    lista_studenti = lista_studenti.order_by("-nume").prefetch_related("cursuri")

    #lista_studenti = Student.objects.boboci()

    context = {
        'studenti': lista_studenti,
        'mesaj': 'Salut'
    }

    return render(request, "lists/list_students.html", context)


def show_curs(request):
    # import pdb; pdb.set_trace()
    # import ipdb; ipdb.set_trace() # pip install ipdb
    id_curs = int(request.GET.get('curs', 0))
    curs = Curs.objects.get(id=id_curs)
    studenti = curs.student_set.all()
    context = {
        'studenti': studenti
    }
    return render(request, "lists/list_curs.html", context)


def process_form(request):
    context= {
        "username": request.GET.get("username"),
        "text": request.POST.get("text")
    }
    return render(request, "form.html", context)

from .forms import ContactForm

def contact(request):
    data = {}
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            data = contact.cleaned_data
    else:
        contact = ContactForm()
    context = {
        "contact_form": contact,
        "data": data
    }
    return render(request, "contact.html", context)

from .forms import StudentForm

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    context = {
        "form": form
    }
    return render(request, "add_student.html", context)

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:   
        form = StudentForm(instance=student)
    context = {
        "form": form
    }
    return render(request, "add_student.html", context)


def session_data(request):
    request.session["view_count"] +=1
    context = {}
    return render(request, "sesiune.html", context)

from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect('/')
