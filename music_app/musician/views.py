from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
# Create your views here.


def create_account(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('musician')
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
            return redirect('musician')
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('musician')


def musician(request):
    musicians = Musician.objects.all()
    return render(request, 'musician.html', {'musicians': musicians})


def add_musician(request):
    musician_form = MusicianForm()
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('musician')
    return render(request, 'add_musician.html', {'form': musician_form})


def edit_musician(request, id):
    try:
        musician = Musician.objects.get(pk=id)
        musician_form = MusicianForm(instance=musician)
        if request.method == 'POST':
            musician_form = MusicianForm(request.POST, instance=musician)
            if musician_form.is_valid():
                musician_form.save()
                return redirect('musician')
        return render(request, 'add_musician.html', {'form': musician_form})
    except:
        return redirect('home')


def delete_musician(request, id):
    try:
        musician = Musician.objects.get(pk=id)
        musician.delete()
        return redirect('home')
    except:
        return redirect('home')
