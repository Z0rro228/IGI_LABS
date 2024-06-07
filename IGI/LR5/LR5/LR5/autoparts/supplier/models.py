from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Suppliers"

    def __str__(self):
        return self.name
