from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2","email"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control '}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),


        }



class LoginForm(forms.Form):
   username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
   password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))