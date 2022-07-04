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
        if student.an > 1:
            student.an = student.an - 1
            student.save()

class StudentAdmin(admin.ModelAdmin):
    # list view specific fields 
    list_display = ('nume', 'prenume', 'an', 'email')
    list_per_page = 10
    list_filter = ['an']
    search_fields = ('nume__startswith', )
    actions = (graduate, picat)
    change_list_template = "admin/change_list_student.html"
    # change view specific fields

    change_form_template = "admin/change_form_student.html"
    readonly_fields = ("an", )
    fieldsets = (
        ('Date personale', {
            'fields': ['prenume', 'nume', 'an']
        })
        ,
        ('Date de contact', {
            'fields': ["email", "telefon"],
            'classes': ['collapse']
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if False:
            self.list_filter.append('email')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.username == "admin":
            qs = qs.filter(an=1)
        return qs

    def save_model(self, request, obj, form, change,):
        obj.nume = obj.nume.title()
        return super().save_model(request, obj, form, change)

admin.site.register(Student, StudentAdmin)

admin.site.register(Curs)

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Membership)

