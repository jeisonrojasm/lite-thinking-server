from django.db import models

# Create your models here.


class Enterprise(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    nit = models.PositiveIntegerField(primary_key=True, max_length=9)
    tel = models.PositiveIntegerField(max_length=10)
