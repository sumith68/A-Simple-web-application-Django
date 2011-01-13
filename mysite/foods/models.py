from django.db import models

# Create your models here.
class User(models.Model):

    u_name = models.CharField(max_length=200)
    p_word = models.CharField(max_length=200)

class recipe(models.Model):

    ingredients = models.CharField(max_length=200)
    photo= models.CharField(max_length=200)
    recipesteps = models.CharField(max_length=200)
  

