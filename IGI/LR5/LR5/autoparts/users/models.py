from datetime import date

import pytz
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField('is_admin', default=False)
    is_customer = models.BooleanField('is_customer', default=False)
    is_employee = models.BooleanField('is_employee', default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    current_discount = models.IntegerField(default=0)

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year
            if today.month < self.date_of_birth.month or (
                    today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                age -= 1
            return age
        return None


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=None)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, default="")
    current_discount = models.IntegerField(default=0)

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year
            if today.month < self.date_of_birth.month or (
                    today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                age -= 1
            return age
        return None

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}"
