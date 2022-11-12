
from django.contrib.auth import authenticate , login
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request,'authentication\index.html')

def signup(request):
    if request.method=="POST" :
     user_name=request.POST.get("username", "default value")
     email_id=request.POST.get("emailid", "default value")
     pass_word=request.POST.get("password", "default value")
     cpass_word=request.POST.get("cpassword", "default value")
     d_name=request.POST.get("dname", "default value")
     if (pass_word==cpass_word):
        myuser=User.objects.create_user(username=user_name,email=email_id,password=pass_word)
        myuser.displayname=d_name
        myuser.save()
        return redirect('index')

    return render(request,'authentication\signup.html')

def userlogin(request):
   if request.method=="POST" :
     uname=request.POST["username"]
     pswd=request.POST["password"]
     user=authenticate(username=uname,password=pswd)
     if user is  not None:
        login(request,user)
        return render(request,'authentication\index.html')
     else :
        messages.error(request,"bad credentials")
        return render(request,r"authentication\\userlogin.html")
   else:     
    return render(request,r'authentication\\userlogin.html')   

def signout(request):
    pass