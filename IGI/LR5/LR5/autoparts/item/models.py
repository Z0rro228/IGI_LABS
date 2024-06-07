from datetime import datetime

from django.db import models
from supplier.models import Supplier
from deal.models import Deal


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)
    article = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    quantity = models.IntegerField(default=1)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", default="images/no_image.jpg", verbose_name="Загрузите фото товара")
    is_sold = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name
