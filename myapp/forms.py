from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","email","first_name","last_name","password"]

class SignInForm(forms.Form):      #inherited from normal form since there isn't create or update

    username=forms.CharField()

    password=forms.CharField()

    