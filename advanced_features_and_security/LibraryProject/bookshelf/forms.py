from django import forms

# class ExampleForm(forms.Form):
#     name = forms.CharField(label ='Your name', max_length=100)
#     email = forms.CharField(label='Email Address')

class ExampleForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Email Address')