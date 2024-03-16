from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(unique=True)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=30) 
    description = models.CharField(max_length=5000)
    amount = models.IntegerField(validators=[MinValueValidator(limit_value=1)] )
    rating = models.IntegerField(default=0)
    total_rates = models.IntegerField(default=0)
    reviews = ArrayField(models.CharField(max_length=3000), blank=True, default=list)
    image = models.ImageField(upload_to='./book/static/book')


    def __str__(self):
        return self.title