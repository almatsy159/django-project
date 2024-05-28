from django.db import models

# Create your models here.
"""
class Lambda(models.Model):
    name = models.CharField(max_length=50)
    
class Kappa(models.Model):
    value = models.IntegerField(max_length=10)
   
""" 
class Work(models.Model):
    dcrea = models.DateTimeField()
    name = models.CharField(max_length=20)
