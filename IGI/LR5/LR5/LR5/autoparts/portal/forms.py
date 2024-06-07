from django import forms

from .models import Feedback, FAQ, UserFAQ
from utils.get_faqs import get_faqs


class FeedbackForm(forms.ModelForm):
    feedback = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            }
        )
    )

    rate = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Оценка'
            }
        )
    )

    class Meta:
        model = Feedback
        fields = ['feedback', 'rate']


class FAQCreationForm(forms.ModelForm):
    question = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос'
            }
        )
    )

    answer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ответ'
            }
        )
    )

    class Meta:
        model = FAQ
        fields = ['question', 'answer']


class FAQUpdateForm(forms.ModelForm):
    question = forms.ChoiceField(
        choices=get_faqs
    )

    new_question = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Новый вопрос'
            }
        )
    )

    new_answer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Новый ответ'
            }
        )
    )

    class Meta:
        model = UserFAQ
        fields = ['question', 'new_question', 'new_answer']


class FAQDeleteForm(forms.Form):
    question = forms.ChoiceField(
        choices=get_faqs
    )
