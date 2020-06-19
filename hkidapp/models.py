from django.db import models

# Create your models here.
from django.conf import settings

class Customer(models.Model):
    hkid = models.CharField(max_length=8,primary_key=True)
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    dob = models.DateField()