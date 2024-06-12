from django.db import models

from store.models import BaseModel


class Supplier(BaseModel):
    name = models.CharField(max_length=255)
    contact = models.TextField()

    def __str__(self):
        return self.name


class Item(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    suppliers = models.ManyToManyField(Supplier, related_name="items")

    def __str__(self):
        return self.name
