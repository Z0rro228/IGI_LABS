from django.urls import re_path

from .views import get_statistics

urlpatterns = [
    re_path(r"^statistic/$", get_statistics, name="statistics")
]
