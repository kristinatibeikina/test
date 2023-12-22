from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    types = (('Товар', 'Товар'), ('Услуга', 'Услуга'))
    type = models.CharField(choices=types, max_length=6)
    image = models.ImageField(upload_to='media/')

