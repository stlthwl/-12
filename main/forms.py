from django.forms import ModelForm, TextInput, Textarea
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone", "message"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Как к Вам обращаться?'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон в формате +79991234567'
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст сообщения'
            })
        }