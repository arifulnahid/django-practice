from django.shortcuts import render, redirect
from . import models
from .forms import AppForm, AppModelForm

# Create your views here.


def get_form(request):
    app_form = AppForm()
    return render(request, 'app.html', {'form': app_form})


def model_form(request):
    app_form = AppModelForm()
    return render(request, 'app.html', {'form': app_form})
