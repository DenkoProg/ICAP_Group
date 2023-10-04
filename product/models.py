from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()
    category = models.CharField(max_length=255)
    offer_of_the_month = models.BooleanField(default=False)
    availability = models.BooleanField(default=False)
    self_pickup = models.BooleanField(default=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

