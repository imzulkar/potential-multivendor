from django.db import models

from authentications.models import User
from core.models import BaseModel
from product_management.models import Product


class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cart} - {self.product}"