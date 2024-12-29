from django.db import models

from authentications.models import User
from core.models import BaseModel
from product_management.models import Product


# Create your models here.
class Order(BaseModel):
    """
    Order created during checkout.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)


class OrderItem(BaseModel):
    """
    Items in an order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)