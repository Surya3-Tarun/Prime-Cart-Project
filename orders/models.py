from django.db import models
from products.models import Product


class Order(models.Model):

    STATUS_CHOICES = [

        ('Ordered','Ordered'),
        ('Shipped','Shipped'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled'),

    ]

    name = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    address = models.TextField()

    landmark = models.CharField(max_length=200, blank=True)

    city = models.CharField(max_length=100, blank=True)

    pincode = models.CharField(max_length=10, blank=True)

    total_price = models.IntegerField()

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Ordered'
    )

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f"Order #{self.id}"



class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    price = models.FloatField()


    class Meta:

        verbose_name = "Ordered Item"

        verbose_name_plural = "Ordered Items"


    def __str__(self):

        return self.product.name