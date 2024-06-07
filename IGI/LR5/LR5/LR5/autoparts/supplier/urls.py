from django.urls import re_path

from .views import get_all_suppliers

urlpatterns = [
    re_path(r"^suppliers/$", get_all_suppliers, name="suppliers"),
]