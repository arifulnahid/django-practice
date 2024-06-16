from django.urls import path
from . import views

urlpatterns = [
    path('', views.album, name='album'),
    path('add-album/', views.add_album, name='add_album'),
    path('edit-album/<int:id>', views.edit_album, name='edit_album'),
    path('delete-album/<int:id>', views.delete_album, name='delete_album'),
]
