from django.db import models

class Product(models.Model):
	item = models.CharField(max_length=200, default='ITEM')
	quantity = models.CharField(max_length=200, default='QUANTITY')
	price = models.CharField(max_length=200, default='PRICE')
# Create your models here.
