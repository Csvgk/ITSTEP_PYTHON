from django import forms

from .models import Comment, Subscriber


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Ваш коментар'}
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ваш коментар...'}),
        }
        error_messages = {
            'text': {
                'required': 'Коментар не може бути порожнім.',
                'max_length': 'Коментар не може бути довшим за 500 символів.',
            },
        }

    def clean_text(self):
        text = self.cleaned_data.get('text', '').strip()
        if not text:
            raise forms.ValidationError('Коментар не може бути порожнім.')
        if len(text) < 5:
            raise forms.ValidationError('Коментар має містити щонайменше 5 символів.')
        if len(text) > 500:
            raise forms.ValidationError('Коментар не може бути довшим за 500 символів.')
        return text


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
        }
        error_messages = {
            'email': {
                'unique': 'Цей email вже підписаний на новини.',
                'invalid': 'Введіть правильну email-адресу.',
            },
        }

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if Subscriber.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Цей email вже підписаний на новини.')
        return email
