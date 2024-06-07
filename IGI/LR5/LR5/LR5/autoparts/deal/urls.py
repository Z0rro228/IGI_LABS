from django.urls import re_path

from .views import get_deals, buy_item

urlpatterns = [
    re_path(r"^deals/$", get_deals, name="deals"),
    re_path(r"^buy/(?P<item_id>\d+)$", buy_item, name="buy_item"),
]
