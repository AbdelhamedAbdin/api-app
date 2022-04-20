from django.db import models
from decimal import Decimal
import json


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def discount(self):
        return Decimal(self.price)*Decimal(3/100)

    def after_discount(self):
        # return self.price - self.discount
        return "33"


class Post(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def fake_author(self):
        return "default_user"
