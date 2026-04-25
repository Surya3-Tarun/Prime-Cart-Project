from django.db import models

class Coupon(models.Model):

    code = models.CharField(max_length=20)
    discount = models.IntegerField(help_text="Discount %")

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code