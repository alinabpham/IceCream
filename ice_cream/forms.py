from django import forms
from .models import Order, Option
from django.contrib import admin

FLAVORS = (('peanut', 'peanut'), ('raspberry', 'raspberry'), ('cola', 'cola'))
TOPPINGS = (('h', 'h'), ('l', 'l'))
CONTAINERS = (('h', 'h'), ('l', 'l'))


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('flavor', 'toppings', 'container', 'name', 'address', 'phone', 'email',)

    def send_email(self):
        # to send an email
        pass


class OptionForm(forms.ModelForm):

    flavors = forms.CharField(max_length=50, required=False)
    toppings = forms.CharField(max_length=50, required=False)
    containers = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Option
        fields = ('flavors', 'toppings', 'containers')


