from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        #whenever the validation is done new form is created
        model= User
        fields =['username','email','password1', 'password2']