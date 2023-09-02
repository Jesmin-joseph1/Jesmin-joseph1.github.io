from django.contrib.auth.models import User
from django.db import models
from shopapp.models import Product
# Create your models here.
# model class for cart
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, unique=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

# model class for item
class Items(models.Model):
    products = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.products

    def total(self):
        return self.products.price * self.quantity

