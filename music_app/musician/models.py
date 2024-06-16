from django.db import models
from album.models import Album

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    instrument = models.CharField(max_length=20)
    album = models.ManyToManyField(Album)

    def __str__(self):
        return self.first_name + " " + self.last_name
