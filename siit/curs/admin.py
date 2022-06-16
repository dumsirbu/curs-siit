from django.contrib import admin

# Register your models here.
from .models import Student, Curs

class StudentAdmin(admin.ModelAdmin):
    list_display = ('nume', 'prenume', 'email')

admin.site.register(Student, StudentAdmin)

admin.site.register(Curs)

