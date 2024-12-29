from django.db import models
from core.models import BaseModel

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    added_by = models.ForeignKey("authentications.User", on_delete=models.CASCADE, related_name="category_user")

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    added_by = models.ForeignKey("authentications.User", on_delete=models.CASCADE, related_name="sub_category_user")


    def __str__(self):
        return f"{self.name} ({self.category.name})"