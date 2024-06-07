from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .models import Supplier
from utils.user_tests import employee_check


@user_passes_test(employee_check)
def get_all_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, "supplier/suppliers.html", {
        "suppliers": suppliers
    })
