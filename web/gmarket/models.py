from django.db import models
from django.utils.timezone import now

# Create your models here.

class GMarket(models.Model):
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200, primary_key=True)
    price = models.CharField(max_length=200)
    sale = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    create_at = models.DateTimeField(default=now())
