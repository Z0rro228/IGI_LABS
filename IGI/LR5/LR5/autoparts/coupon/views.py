from django.shortcuts import render, redirect

from .forms import CouponForm
from .models import Coupon, UsedUserCoupon


# Create your views here.


def enter_coupon(request):
    if request.method == "POST":
        form = CouponForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = request.user
            coupon = Coupon(name=form.save(commit=False).name)
            all_coupons = Coupon.objects.all()
            print(coupon.name)
            if coupon.name not in [coupon.name for coupon in all_coupons]:
                form.add_error('name', 'Такого купона не существует')
                return render(request, "core/coupons.html", {"form": form})
            coupon.discount = [x.discount for x in all_coupons if x.name == coupon.name][0]
            all_user_coupons = UsedUserCoupon.objects.all()
            print(all_user_coupons)
            if [x for x in all_user_coupons if x.coupon == coupon and x.user == user]:
                form.add_error('name', 'Вы уже использовали этот купон')
                return render(request, "core/coupons.html", {"form": form})
            user.current_discount = coupon.discount
            user_coupon.save()
            user.save()
            return redirect("/")
        else:
            form = CouponForm()
    return render(request, "core/coupons.html", {"form": form})


def coupons_view(request):
    form = CouponForm()
    return render(request, "core/coupons.html", {"form": form})