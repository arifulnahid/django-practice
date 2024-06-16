from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.messages import success
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            success(request, 'Account Create Successful')
            return redirect('profile')
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            success(request, 'Login Successful')
            return render(request, 'profile.html')
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    success(request, 'Logged Out Successful')
    return redirect('login')


@login_required(login_url='/')
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    return redirect('login')


@login_required(login_url='/')
def password_change(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            success(request, 'Password Change Successful')
            return redirect('profile')
    return render(request, 'passwordchnage.html', {'form': form})


@login_required(login_url='/')
def password_reset(request):
    form = SetPasswordForm(request.user)
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            success(request, 'Password Reset Successful')
            return redirect('profile')
    return render(request, 'passwordchnage.html', {'form': form})
