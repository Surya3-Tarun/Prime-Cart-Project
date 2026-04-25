from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} Review"