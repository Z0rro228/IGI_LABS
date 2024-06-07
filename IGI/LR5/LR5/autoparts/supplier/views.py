from django.shortcuts import render, redirect
from .models import Supplier


def get_all_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, "core/suppliers.html", {
        "suppliers": suppliers
    })
