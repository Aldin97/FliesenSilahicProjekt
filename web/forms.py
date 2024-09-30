from django import forms

class ContactForm(forms.Form):
    ime = forms.CharField(label='Name', max_length=100, required=True)
    telefon = forms.CharField(label='Telefon', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    poruka = forms.CharField(label='Nachricht', widget=forms.Textarea, required=True)
