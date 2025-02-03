# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=15, required=False)
    message = forms.CharField(widget=forms.Textarea)