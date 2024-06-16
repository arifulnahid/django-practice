from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician, name='musician'),
    path('signup/', views.create_account, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add-musician', views.add_musician, name='add_musician'),
    path('edit-musician/<int:id>', views.edit_musician, name='edit_musician'),
    path('delete-musician/<int:id>',
         views.delete_musician, name='delete_musician'),
]
