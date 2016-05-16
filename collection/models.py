from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
        symbol = models.CharField(max_length=255)
        name = models.CharField(max_length=255)
        slug = models.SlugField(unique=True)
        user = models.ManyToManyField(User, blank=True)