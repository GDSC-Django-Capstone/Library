from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    borrowed = ArrayField(models.CharField(max_length=200), blank=True)
    history = ArrayField(models.CharField(max_length=200), blank=True)
    banned = models.BooleanField(default=False)
    role = models.CharField(max_length=10)


    def __str__(self):
        return self.email