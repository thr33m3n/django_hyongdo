from django.db import models

# Create your models here.
"""class User데이타는 어떻게?"""

class Restaurant(models.Model):

    subway_line = models.CharField(max_length=30)
    station = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)
    workingtime = models.CharField(max_length=30)
    views = models.IntegerField()
    reviews = models.IntegerField()
    likes = models.IntegerField()
    explanation = models.CharField(max_length=200)
    images = models.ImageField()
