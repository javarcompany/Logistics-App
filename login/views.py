from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.contrib.auth.forms import PasswordChangeForm

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

@login_required(login_url='login')
def change_psw(request):
    if request.method == "POST":
        passwordForm = PasswordChangeForm(request.user, request.POST)
        if passwordForm.is_valid():
            changes = passwordForm.save()
            update_session_auth_hash(request, changes)
            messages.success(request, "Password have modified successfullly/..!")
            return redirect('index')
        else:
            print(passwordForm)
            messages.error(request, "An error was encountered while modifying password..!")
    context = {}
    return render(request, "authentication/change_psw.html", context)