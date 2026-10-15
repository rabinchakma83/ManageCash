from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User    
        fields = ['username','password1','password2']
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)  
    class Meta:
        model = User    
        fields = ['username','password']        