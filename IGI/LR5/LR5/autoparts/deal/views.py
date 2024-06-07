from datetime import datetime

from django.shortcuts import render, redirect

from .forms import DealForm
from .models import Deal


# Create your views here.


def buy_item(request, pk=None):
    if request.method == "POST":
        form = DealForm(request.POST)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.price = pk
            deal.date = datetime.now()
            deal.total_cost = deal.price * deal.quantity * (100 - request.user.current_discount) / 100
            request.user.current_discount = 0
            request.user.save()
            deal.save()
            return redirect("/")
        else:
            form = DealForm()
    return render(request, "core/index.html", {"form": form})


def get_deals(request):
    deals = Deal.objects.all()
    return render(request, "core/deals.html", {"deals": deals})
