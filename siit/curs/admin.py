from django.contrib import admin
from django.db.models import F

# Register your models here.
from .models import Student, Curs, Question, Choice, Membership

@admin.action(description='Promoveaza')
def graduate(modeladmin, request, queryset):
    queryset.update(an=F('an') + 1) # UPDATE SET AN=AN+1 WHERE id in []

@admin.action(description="Pica anul")
def picat(modeladmin, request, queryset):
    for student in queryset:
        student.an = student.an - 1
        student.save()

class StudentAdmin(admin.ModelAdmin):
    list_display = ('nume', 'prenume', 'an', 'email')
    list_per_page = 10
    list_filter = ('an',)
    search_fields = ('nume__startswith', )
    actions = (graduate, picat)

admin.site.register(Student, StudentAdmin)

admin.site.register(Curs)

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Membership)

