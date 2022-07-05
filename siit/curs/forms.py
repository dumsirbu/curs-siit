from xml.dom import ValidationErr
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

    def clean_prenume(self):
        prenume = self.cleaned_data["prenume"]
        if not prenume.title() == prenume:
            raise forms.ValidationError("Trebuie sa inceapa cu litera mare")
        return prenume
    #altceva = forms.CharField(required=False, max_length=200)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)