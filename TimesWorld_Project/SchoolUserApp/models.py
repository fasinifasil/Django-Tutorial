from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

# Create your models here.
User_Role=(('a','student'),('b','staff'),('c','admin'),('d','editor'))
class RegisterData(models.Model):
    username    = models.CharField(max_length=100)
    email   = models.EmailField()
    role    = models.CharField(max_length = 20,choices = User_Role)
    country = CountryField()
    nationality =models.CharField(max_length=30)
    mobile  =models.IntegerField()
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username




