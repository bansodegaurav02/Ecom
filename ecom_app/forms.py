from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class userregistration(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        widgets={
            'Username':forms.TextInput(attrs={"class":"form-control"}),
            'Firts Name':forms.TextInput(attrs={"class":"form-control"}),
            'Last Name':forms.TextInput(attrs={"class":"form-control"}),
            'Email':forms.EmailInput(attrs={"class":"form-control"}),
            'PAssword':forms.PasswordInput(attrs={"class":"form-control"}),
            'Confirm PAssword':forms.PasswordInput(attrs={"class":"form-control"})

        }


class auth_form(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']


class product_form(forms.ModelForm):
    class Meta:
        model=products
        fields=['cat','name','description','prize','images']
      