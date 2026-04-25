from django.db import models
from products.models import Product

class Cart(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name