from datetime import datetime

from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect

from .forms import DealForm
from .models import Deal
from item.models import Item

from utils.user_tests import employee_check


# Create your views here.

@login_required
def buy_item(request, item_id):
    if request.method == "POST":
        form = DealForm(request.POST)
        if form.is_valid():
            item = Item.objects.filter(id=item_id)[0]
            deal = form.save(commit=False)
            deal.price = item.price
            deal.date = datetime.now()
            deal.total_cost = deal.price * deal.quantity * (100 - request.user.current_discount) / 100
            request.user.current_discount = 0
            item.quantity -= deal.quantity
            item.quantity_sold += deal.quantity
            item.save()
            request.user.save()
            deal.save()
            return redirect("/")
        else:
            form = DealForm()
    return render(request, "core/index.html", {"form": form})


@user_passes_test(employee_check)
def get_deals(request):
    deals = Deal.objects.all()
    return render(request, "deal/deals.html", {"deals": deals})
