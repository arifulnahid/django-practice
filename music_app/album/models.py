from django.db import models

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=15)
    release_date = models.DateField()
    rating = models.CharField(max_length=1,
                              choices=(('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)), default=1)

    def __str__(self):
        return self.name
