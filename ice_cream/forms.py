from django import forms
from .models import Order, Option


class OrderForm(forms.ModelForm):
    flavor = forms.ModelChoiceField(queryset=Option.objects.all().filter(group='flavor'))
    toppings = forms.ModelMultipleChoiceField(queryset=Option.objects.all().filter(group='topping'), widget=forms.CheckboxSelectMultiple, required=False)
    container = forms.ModelChoiceField(queryset=Option.objects.all().filter(group='container'))
    email = forms.EmailField()

    class Meta:
        model = Order
        fields = ('flavor', 'toppings', 'container', 'name', 'address', 'phone', 'email',)
