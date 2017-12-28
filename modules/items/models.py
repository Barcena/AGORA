from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from modules.business.models import B2cProfile



class Item(models.Model):
    # associations
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    business      	= models.ForeignKey(B2cProfile, on_delete=models.CASCADE)
    name            = models.CharField(max_length=120)
    description     = models.TextField(max_length = 280)
    extra_info      = models.TextField(max_length = 280)
    politicas       = models.TextField(max_length = 280)
    price           = models.IntegerField(default=0)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self): 
         
        return reverse('items:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp']