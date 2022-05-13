from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField

# Create your models here.

class Event(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.slug
    
    

    

class Item(models.Model):
    nome: models.CharField("Nome", max_length= 50, unique=False, blank= False)
    name: models.TextField(max_length=50, unique= True)
    description = models.TextField(blank = True, null = True)
    value: models.IntegerField('Value', blank= False)
    
    def __str__(self):
        return self.description
   