from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm #form
from django.contrib import messages#flash mesajları
from django.contrib.auth.models import User #kullanıcı ekleme
from django.contrib.auth import login, authenticate, logout #kullanıcıyı login etme


# Create your views here.

def register(request):
#YÖNTEM-1
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save() #kayıt işlemi
        login(request,newUser)#kullanıcının login işlemi

        messages.info(request,"Başarıyla kayıt oldunuz") #flash messajları, django messages

        return redirect("index")
    else:
        context = {
            "form" : form
        }
        return render(request,"register.html",context)
"""
YÖNTEM-2

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)

            return redirect("index")
        else:
            context = {
                "form" : form
            }
            return render(request,"register.html",context)

    else:
        form = RegisterForm()
        context = {
        "form" : form
        }
        return render(request,"register.html",context)"""

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)
        
        messages.success(request, "Başarıyla Giriş Yaptınız...")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış Yaptınız...")
    return redirect("index")
