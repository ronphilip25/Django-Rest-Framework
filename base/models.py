from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null="")
    created = models.DateTimeField(auto_now_add=True)
    