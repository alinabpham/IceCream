from django import forms
from .models import Order, Topping


class OrderForm(forms.ModelForm):
    toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Order
        fields = ('flavor', 'toppings', 'container', 'name', 'address', 'phone', 'email',)
