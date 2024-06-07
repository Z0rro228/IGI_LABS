from django import forms

from .models import Deal


class DealForm(forms.ModelForm):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }
        )
    )

    class Meta:
        model = Deal
        fields = ['quantity']
