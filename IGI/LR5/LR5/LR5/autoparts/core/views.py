import datetime
import re

import pytz
from django.shortcuts import render, redirect
from django.utils import timezone
import logging

from item.models import Item

from deal.forms import DealForm

from portal.forms import FeedbackForm

from .forms import SearchForm

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')


# Create your views here.


def index(request):
    items = filter(lambda x: x.quantity > 0, Item.objects.all())
    if "text" in request.GET:
        items = filter(lambda x: re.search(request.GET["text"], x.name), items)
    tz = timezone.get_current_timezone().tzname(datetime.datetime.now())
    current_date = datetime.datetime.now().date()
    search_form = SearchForm()
    items = list(items)
    if "sorting" in request.GET and request.GET["sorting"] == "2":
        items.sort(key=lambda x: x.price, reverse=True)
    else:
        items.sort(key=lambda x: x.price)

    return render(request, "core/index.html", {
        "items": items,
        "form": DealForm,
        "feedback_form": FeedbackForm,
        "search_form": search_form,
        "tz": tz,
        "current_date": current_date
    })
