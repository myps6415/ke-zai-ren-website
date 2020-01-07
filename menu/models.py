from django.db import models

# Create your models here.
class menu(models.Model):
    item = models.TextField(blank=False)
    price = models.IntegerField(blank=False)
    can_sell = models.BooleanField(blank=False)
    photo = models.URLField(blank=True)