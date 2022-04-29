from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SingUp (UserCreationForm):
    user_name = forms.CharField()
    email = forms.EmailField()
    pass1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    pass_conf = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

class Avatar (forms.form):
    thumbnail = forms.ImageField()    

