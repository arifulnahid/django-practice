from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_form, name='app'),
    path('app-form', views.get_form, name='app_form'),
    path('model-form', views.model_form, name='model_form'),
]
