from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    age = models.IntegerField()
