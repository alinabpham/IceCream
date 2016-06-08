from django import forms
from .models import Order, Flavor, Topping, Container
from django.contrib import admin


class OrderForm(forms.ModelForm):
    flavor = forms.ModelChoiceField(queryset=Flavor.objects.all())
    toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    container = forms.ModelChoiceField(queryset=Container.objects.all())
    email = forms.EmailField()

    class Meta:
        model = Order
        fields = ('flavor', 'toppings', 'container', 'name', 'address', 'phone', 'email',)

    def send_email(self):
        # to send an email
        pass