from django.shortcuts import render, redirect
from home.views import homepage # Importing the homepage view from the home app

from . forms import UserCreation, UserLogin # Importing the UserCreation form and the signup form
from django.contrib import messages


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def home(request):
    return homepage(request)

def sign_up(request):
    form = UserCreation()
    
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return render(request, 'authentication_app/login.html')
        else:
            form = UserCreation()
        
    return render(request, 'authentication_app/sign-up.html', {'signup_form': form})

def login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if user.roleType == 'admin':
                    return redirect('admin-dashboard')
                else:
                    return redirect('dashboard')
            else:
                messages.info(request, 'Username OR Password is incorrect')
                form = UserLogin()

    return render(request, 'authentication_app/login.html', {'login_form': form})



def logout(request):
    auth.logout(request)
    return redirect('sign')

def dashboard(request):
    pass


