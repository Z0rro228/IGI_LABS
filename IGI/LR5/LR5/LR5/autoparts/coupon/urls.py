from django.urls import re_path

from .views import enter_coupon

urlpatterns = [
    re_path(r'^coupons/$', enter_coupon, name='enter_coupon')
]
