from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from . models import Vault, APIKeyEntry

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        
        if password != confirmPassword:
            messages.error(request, "Password doesn't match.")
        elif User.objects.filter(username=username).exists:
            messages.error(request, "Username already taken.")
        else:
            user = User.objects.create_user(username=username, email=email,password=password)
            login(request, user)
            return redirect('dashboard')
        
    return render(request, 'vault/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalide username or password.")
    return render(request, 'vault/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    vault, _ = Vault.objects.get_or_create(name='Default', owner=request.user)
    keys = APIKeyEntry.objects.filter(vault__owner=request.user)
    return render(request, 'vault/dashboard.html', {'keys' : keys})

