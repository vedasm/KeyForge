from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'vault/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'vault/dashboard.html')  