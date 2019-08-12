from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
