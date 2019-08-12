from django.db import models

class Visualization(models.Model):
	antecedents = models.CharField(max_length=200, default='ANTECEDENTS')
	consequents = models.CharField(max_length=200, default='CONSEQUENTS')
	antecedent_support = models.CharField(max_length=200, default='ANTECEDENT_SUPPORT')
	consequent_support = models.CharField(max_length=200, default='CONSEQUENT_SUPPORT')
	support = models.CharField(max_length=200, default='SUPPORT')
	confidence = models.CharField(max_length=200, default='CONFIDENCE')
	lift = models.CharField(max_length=200, default='LIFT')
	leverage = models.CharField(max_length=200, default='LEVERAGE')
	conviction = models.CharField(max_length=200, default='CONVICTION')
	
# Create your models here.
