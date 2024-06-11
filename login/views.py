from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *

# Create your views here.
@login_required(login_url = 'login')
def index(request):
    print("I am in the Home Page")

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    login_form = UserLogInForm(request.POST or None)
    if request.method == "POST":
        userid = request.POST.get('username')
        passcode = request.POST.get("password")

        userauth = authenticate(request = request, username = userid, password = passcode)

        if userauth is not None:
            login(request, userauth)
            messages.info(request, "Log In Successfull.....")
            return redirect('index')
        else:
            messages.error(request, "Incorrect User Name or Password")

    context = {"login_form":login_form}
    return render(request, 'authentication/login.html', context)

def logoutuser(request):
    messages.warning(request, "You are out of the system")
    logout(request)
    return redirect('login')