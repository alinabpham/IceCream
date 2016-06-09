from django.shortcuts import render, redirect
from django import forms
from .forms import OrderForm
import datetime
from .models import Flavor, Topping, Container
from django.core.mail import send_mail


def send_email_to_claire(body, name):
    email_body = 'A new order for ice cream was made by ' + name + '.\n\n' + \
                body
    send_mail('New Order',
              email_body,
              'claires.icecream.order@gmail.com',
              ['meyer.alexander.john@gmail.com'],
              fail_silently=False
              )


def send_email_to_customer(body, name, to_email):
    email_body = name + ',\n\n' + "Thank you for ordering from Claire's Creamery! Your order details are as follows:" + \
                '\n\n' + body + '\n\n' + "Let us know if there are any issues, but mostly, enjoy that " + \
                "ice cream!\n\nYour sweet tooth savior,\nClaire's Creamery"
    send_mail('Your Order',
              email_body,
              'claires.icecream.order@gmail.com',
              [to_email],
              fail_silently=False
              )


def orderview(request):

    def get_topping_str():
        toppings_str = ''
        for topping in form.cleaned_data.get('toppings'):
            toppings_str += str(topping) + ', '
        toppings_str = toppings_str[:-2]

        return toppings_str

    def make_order_body():
        order_body = 'Flavor: ' + order.flavor + '\n' + \
                     'Container: ' + order.container
        toppings_str = get_topping_str()
        # if not empty, show toppings
        if len(toppings_str) > 0:
            order_body += '\n' + 'Toppings: ' + toppings_str

        return order_body

    form = OrderForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            order = form.save(commit=False)
            order.order_time = datetime.datetime.now()
            order.toppings = get_topping_str()
            order.save()

            body = make_order_body()
            send_email_to_claire(body, order.name)
            send_email_to_customer(body, order.name, order.email)

            # once ordered, redirect
            return redirect('success/')

    return render(request, 'ice_cream/order.html', {'form': form})


def optionview(request, option_type):

    type_model_dict = {
        'flavors': Flavor,
        'toppings': Topping,
        'containers': Container,
    }

    type_tagline_dict = {
        'flavors': 'Flavors to Savor',
        'toppings': "Poppin' Toppin's",
        'containers': 'No-Brainer Containers'
    }

    def get_context_data():

        def get_tagline(option_type):
            return type_tagline_dict[option_type]

        context = dict()
        context['option_type_cap'] = option_type.capitalize()
        context['tagline'] = get_tagline(option_type)

        option_qs = type_model_dict[option_type].objects.all()

        option_list = []
        for option in option_qs:
            option_list.append((str(option), str(option.image)))

        context['option_list'] = option_list

        return context

    context = get_context_data()
    # how to make this path just choices?
    return render(request, 'ice_cream/choices.html', context)
