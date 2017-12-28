from django.db import models
from django.contrib.auth.models import User



class ToDo(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField()
  