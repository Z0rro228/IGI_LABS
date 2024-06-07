from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CouponForm
from .models import Coupon, UsedUserCoupon


# Create your views here.
@login_required
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
                return render(request, "coupon/coupons.html", {"form": form})
            coupon = [x for x in all_coupons if x.name == coupon.name][0]
            all_user_coupons = UsedUserCoupon.objects.all()
            if coupon.is_archived:
                form.add_error('name', 'Этот купон недействителен')
                return render(request, "coupon/coupons.html", {"form": form})
            if [x for x in all_user_coupons if x.coupon == coupon and x.user == user]:
                form.add_error('name', 'Вы уже использовали этот купон')
                return render(request, "coupon/coupons.html", {"form": form})
            user.current_discount = coupon.discount
            user_coupon = UsedUserCoupon(user=request.user, coupon=coupon)
            user_coupon.save()
            user.save()
            return redirect("/")
    form = CouponForm()
    coupons = Coupon.objects.all()
    return render(request, "coupon/coupons.html", {"form": form, "coupons": coupons})
