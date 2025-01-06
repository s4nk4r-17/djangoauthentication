from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import SignUpForm,SignInForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate

# Create your views here.

class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignUpForm()

        return render(request,"signup.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=SignUpForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data) #create user for hashing password

            print("=====account created=====")

            return redirect("signin")
        
        else:   

            print("xxxxxfailedxxxx")

        return render(request,"signup.html",{"form":form_instance})
    
class SignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignInForm()

        return render(request,"signin.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=SignInForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data #{username:"django",password:"Password@123"}

            uname=data.get("username")

            pwd=data.get("password")

            print(uname,pwd)

            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:

                print("Valid")

            else:

                print("invalid")

            return redirect("signin")

            








# django.contrib.auth
# models
# AbstractBaseUser(password)
# AbstractUser(username,email,first_name,last_name)
# User