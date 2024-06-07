from itertools import accumulate

from django.shortcuts import render
import numpy as np

from users.models import CustomUser

from deal.models import Deal

from item.models import Item

from users.views import calculate_age


# Create your views here.


def get_statistics(request):
    clients = list(filter(lambda x: x.user.is_customer, CustomUser.objects.all()))
    print(clients)
    clients.sort(key=lambda x: x.user.first_name)
    deals = Deal.objects.all()
    deals_sum = 0
    for deal in deals:
        deals_sum += deal.total_cost
    items = list(Item.objects.all())
    items.sort(key=lambda x: x.quantity_sold, reverse=True)
    total_revenue = 0
    for item in items:
        total_revenue += (item.price - item.supplier_price) * item.quantity_sold
        print(item.price, item.supplier_price, item.quantity_sold)
    ages_of_clients = np.array([calculate_age(x.user.date_of_birth) for x in clients])
    ages_mean = ages_of_clients.mean()
    ages_median = np.median(ages_of_clients)
    return render(request, "app_statistics/statistics.html", {
        "clients": clients,
        "deals_sum": deals_sum,
        "total_revenue": total_revenue,
        "sorted_items": items,
        "ages_mean": ages_mean,
        "ages_median": ages_median
        })


