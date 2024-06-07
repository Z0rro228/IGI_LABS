from django import forms

from .models import Feedback, FAQ, UserFAQ


class FeedbackForm(forms.ModelForm):
    feedback = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            }
        )
    )

    class Meta:
        model = Feedback
        fields = ['feedback']


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
    choices = []

    def __init__(self, choices):
        super(FAQUpdateForm, self).__init__()
        self.fields['question'].choices = choices
        self.choices = choices

    question = forms.ChoiceField(
        choices=choices
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
    choices = []

    def __init__(self, choices):
        super().__init__()
        self.fields['question'].choices = choices

    question = forms.ChoiceField(
        choices=()
    )
