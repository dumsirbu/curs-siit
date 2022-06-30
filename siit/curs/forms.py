from django import forms

from .models import Student

class ContactForm(forms.Form):
    nume = forms.CharField(max_length=10, required=False, label="Numele tau")
    email = forms.EmailField()
    text = forms.CharField(max_length=2048, widget=forms.Textarea(attrs = {"class" : "red"}))
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ("cursuri", )
    #altceva = forms.CharField(required=False, max_length=200)
