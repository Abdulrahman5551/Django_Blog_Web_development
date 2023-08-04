from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
# Create your views here.


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect("home")
        else:
            print("Nooo")
            return render(request, 'users/register.html', {'form': form})
        
def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
             return redirect('home')
        
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'users/login.html', {'form': form})
        else:
            print("Noooooooooooo")
            return render(request, 'users/login.html', {'form': form})
    
def sign_out(request):
    logout(request)
    return redirect('home')