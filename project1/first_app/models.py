from django.db import models

# Create your models here.


class App(models.Model):
    id = models.AutoField(primary_key=True)
    binary_data = models.BinaryField()
    boolean_field = models.BooleanField()
    date_time = models.DateTimeField()
    decimal_field = models.DecimalField(decimal_places=2, max_digits=10)
    durations = models.DurationField()
    ip_address = models.GenericIPAddressField()
