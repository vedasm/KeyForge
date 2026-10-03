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
        elif User.objects.filter(username=username).exists():
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
            messages.error(request, "Invalid username or password.")
    return render(request, 'vault/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    vault, _ = Vault.objects.get_or_create(name='Default', owner=request.user)
    keys = APIKeyEntry.objects.filter(vault__owner=request.user)
    return render(request, 'vault/dashboard.html', {'keys' : keys})

@login_required
def add_key(request):
    if request.method == 'POST':
        vault, _ = Vault.objects.get_or_create(name='Default', owner=request.user)
        entry = APIKeyEntry(
            vault=vault,
            name=request.POST.get('name'),
            provider=request.POST.get('provider', ''),
        )
        entry.set_value(request.POST.get('value'))
        entry.save()
        messages.success(request, 'Key added successfully.')
        return redirect('dashboard')
    return render(request, 'vault/add.html')

@login_required
def update_key(request, key_id):
    entry = get_object_or_404(APIKeyEntry, id=key_id, vault__owner=request.user)
    if request.method == 'POST':
        entry.name = request.POST.get('username', entry.name)
        new_value = request.POST.get('password')
        if new_value:
            entry.set_value(new_value)
        entry.save()
        return redirect('dashboard')
    return render(request, 'vault/update.html', {'cred':entry})

@login_required
def delete_key(request, key_id):
    entry = get_object_or_404(APIKeyEntry, id=key_id, vault__owner=request.user)
    if request.method == 'POST':
        entry.delete()
    return redirect('dashboard')

@login_required
def account(request):
    return render(request, 'vault/account.html')