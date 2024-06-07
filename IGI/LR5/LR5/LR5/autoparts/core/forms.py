from django import forms

SORTING_CHOICES = [
    (1, "Сначала дешевые"),
    (2, "Сначала дорогие")
]


class SearchForm(forms.Form):
    text = forms.CharField(max_length=100, required=False)
    sorting = forms.ChoiceField(choices=SORTING_CHOICES)
