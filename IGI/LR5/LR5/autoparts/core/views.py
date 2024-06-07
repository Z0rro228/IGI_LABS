import datetime
import re

from django.shortcuts import render, redirect
import logging

from item.models import Item

from deal.forms import DealForm

from portal.forms import FeedbackForm

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')


# Create your views here.


def index(request):
    items = Item.objects.all()

    return render(request, "core/index.html", {
        "items": items,
        "form": DealForm,
        "feedbacK_form": FeedbackForm
    })
