from django import forms

class ContactForm(forms.Form):
    nume = forms.CharField(max_length=100)
    email = forms.EmailField()
    text = forms.CharField(max_length=2048)
    