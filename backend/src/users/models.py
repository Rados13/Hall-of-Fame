from djongo import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
