from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_mail(self):
        email = self.cleaned_data.get("email")
        if User.object.filter(email__iexact=email).exists():
            raise forms.ValidationError('Tis email has already been registered')
        return email