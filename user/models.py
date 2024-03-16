from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    borrowed = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    history = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    banned = models.BooleanField(default=False)
    role = models.CharField(max_length=10)


    def __str__(self):
        return self.email



class Tracker(models.Model):
    tracking = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    fname = models.CharField(max_length=30, blank=True)
    lname = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=200, blank=True)
    uid = models.IntegerField(blank=True)
    bid = models.IntegerField(blank=True)


    def __str__(self):
        return self.tracking