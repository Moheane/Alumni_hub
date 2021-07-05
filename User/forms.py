from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


class UserRegister(UserCreationForm):
    names = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    dob = forms.CharField()
    Degree = forms.CharField()

    class Meta:
        model = User
        fields = ['names', 'surname', 'email', 'dob', 'Degree',  'username','password1', 'password2']
    