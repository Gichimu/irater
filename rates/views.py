from django.shortcuts import render
from allauth.account.forms import LoginForm, ChangePasswordForm, SignupForm
from allauth.account.views import LoginView, 


def home(request):
    title = 'Home'
    return render(request, 'index.html', {'title': title})

def signup(request):
    form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def login(request):
    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def changePassword(request):
    form = ChangePasswordForm()
    return render(request, 'registration/changepassword.html', {'form': form})