from django.db import models

from authentications.models import User
from core.models import BaseModel
from product_management.models import Product


# Create your models here.
class Order(BaseModel):
    """
    Order created during checkout.
    """
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

    user = models.ForeignKey("authentications.User", on_delete=models.CASCADE, related_name="orders")

    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Order #{self.id} by {self.user.email}"


class OrderItem(BaseModel):
    """
    Items in an order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return  f"{self.order}"

class OrderShipping(BaseModel):
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name="shipping")
    shipping_name = models.CharField(max_length=255, blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    shipping_phone = models.CharField(max_length=15, blank=True, null=True)