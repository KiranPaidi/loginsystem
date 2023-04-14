from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from StudentApp.models import Student


# Create your views here.
def home(request):
    return render(request,'home.html')


def login_fun(request):
    return render(request,'login.html')


def register_fun(request):
    return render(request,'register.html')


def read_register(request):
    username=request.POST['tbuser']
    password=request.POST['tbpass']
    email=request.POST['tbmail']
    u=User.objects.create_superuser(username=username,password=password,email=email)
    u.save()
    return render(request,'login.html',{'msg':f'User Created Sucessfully username as {username}'})


def read_login(request):
    username = request.POST['tbuser']
    password = request.POST['tbpass']
    user=authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        b = Student.objects.all()
        return render(request,'displaystudent.html',{'data':b})
    else:
        return render(request,'login.html')


def logout_fun(request):
    logout(request)
    return redirect('login')