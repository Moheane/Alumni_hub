from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegister

# Create your views here.

def registerView(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Well done {username}! your account has been created.')
            return redirect('user-login')
    else:
            form = UserRegister()
    return render(request, 'User/register.html', {'form':form})


def loginView(request):
    form = UserCreationForm()
    return render(request, 'User/register.html', {'form':form})


def logoutView(request):
    return render(request, 'User/logout.html')

@login_required
def profileView(request):
    return render(request, 'User/profile.html')