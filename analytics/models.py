from django.db import models

# Create your models here.
class PlatformAnalytics(models.Model):
    total_vendors = models.PositiveIntegerField(default=0)
    total_products = models.PositiveIntegerField(default=0)
    total_orders = models.PositiveIntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
