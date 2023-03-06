from django.contrib.auth.models import User
from .models import *
from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,  UserChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Usuario",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Contraseña",                
                "class": "form-control"
            }
        ))


class UserForm(UserCreationForm):
   
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Nombre de Usuario",                
                "class": "form-control"
            }
        ))
    
    
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Contraseña",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Confirmar contraseña",                
                "class": "form-control"
            }
        ))

    
    class Meta:
        model = User
        fields = ('username',  'password1', 'password2', )

    def save(self, commit=True):
        user =super(UserForm, self).save(commit=False)
       
        

        if commit:
            user.save()
        return user