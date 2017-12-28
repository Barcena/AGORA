from django.db import models

# Create your models here.
class Partner(models.Model):
	
	partner_name = models.CharField(max_length=100,default='')
	description = models.CharField(max_length=100, default='')
	promotion = models.CharField(max_length=100,default='')
	promotion = models.CharField(max_length=100,default='')
	webpage = models.URLField(default='')
	phone = models.IntegerField(default=0)