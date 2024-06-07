from django import forms

from .models import UserCoupon


class CouponForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Промокод'
            }
        )
    )

    class Meta:
        model = UserCoupon
        fields = ['name']
