from django.db import models


class Deal(models.Model):
    date = models.DateTimeField()
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    total_cost = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Deals"

    def __str__(self):
        return str(self.date)
