from django.db import models

from core.base_model import BaseModel
from file.models import File


class Product(BaseModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ForeignKey(File, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=21, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=21, decimal_places=2)
    images = models.ManyToManyField(File)
    characteristics = models.TextField()
    attribute_fields = models.ForeignKey('AttributeValue')
    is_available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

