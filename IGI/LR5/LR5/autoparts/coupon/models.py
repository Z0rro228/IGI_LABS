from django.db import models

from users.models import User


# Create your models here.


class Coupon(models.Model):
    name = models.CharField(max_length=16, primary_key=True)
    discount = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Coupons"

    def __str__(self):
        return self.name


class UsedUserCoupon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)


class UserCoupon(models.Model):
    name = models.CharField(max_length=16)