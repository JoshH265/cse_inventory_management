from django.shortcuts import render, redirect
from home.views import homepage # Importing the homepage view from the home app

from . forms import UserCreation # Importing the UserCreation form
from django.contrib import messages

def home(request):
    return homepage(request)

def signup(request):
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
        
    return render(request, 'authentication_app/signup.html', {'signup_form': form})

def login(request):
    return render(request, 'authentication_app/login.html')

def dashboard(request):
    pass


