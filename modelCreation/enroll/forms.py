from django import forms

class StudentRegestration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()