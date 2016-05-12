from django.db import models


class Stock(models.Model):
        symbol = models.CharField(max_length=255)
        name = models.CharField(max_length=255)
        slug = models.SlugField(unique=True)