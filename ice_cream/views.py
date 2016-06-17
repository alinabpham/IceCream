from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.timezone import now
from django.views import generic
from .models import Flavor, Topping, Container
from .forms import OrderForm

TYPE_TAGLINE_DICT = {
    'flavors': 'Flavors to Savor',
    'toppings': "Poppin' Toppin's",
    'containers': 'No-Brainer Containers'
}

MODEL_TYPE_DICT = {
    Flavor: 'flavors',
    Topping: 'toppings',
    Container: 'containers'
}


def get_topping_str(order):
    toppings_str = ''
    for topping in order.toppings.all():
        toppings_str += str(topping) + ', '
    toppings_str = toppings_str[:-2]

    return toppings_str


def email_to_customer(order):
    context = {
        'name': order.name,
        'flavor': order.flavor,
        'toppings': get_topping_str(order),
        'container': order.container,
    }

    message = render_to_string('ice_cream/email_to_customer.html', context)

    send_mail('Your Order',
              message,
              'claires.icecream.order@gmail.com',
              [order.email],
              fail_silently=False
              )


def email_to_claire(order):
    context = {
        'name': order.name,
        'flavor': order.flavor,
        'toppings': get_topping_str(order),
        'container': order.container,
    }

    message = render_to_string('ice_cream/email_to_claire.html', context)

    send_mail('New Order',
              message,
              'claires.icecream.order@gmail.com',
              ['meyer.alexander.john@gmail.com'],
              fail_silently=False
              )


class OrderView(generic.FormView):
    form_class = OrderForm
    success_url = 'success/'
    template_name = 'ice_cream/order.html'

    def form_valid(self, form):
        order = form.save(commit=False)
        order.order_time = now()
        order.save()

        email_to_customer(order)
        email_to_claire(order)

        return super().form_valid(form)


class OptionView(generic.ListView):
    template_name = 'ice_cream/choices.html'

    @property
    def get_type(self):
        return MODEL_TYPE_DICT[self.model]

    @property
    def get_tagline(self):
        return TYPE_TAGLINE_DICT[self.get_type]

    def get_context_data(self, **kwargs):
        context = dict()
        context['option_type_cap'] = self.get_type.capitalize()
        context['tagline'] = self.get_tagline
        context['option_list'] = self.get_queryset()

        return context


class FlavorView(OptionView):
    model = Flavor


class ToppingView(OptionView):
    model = Topping


class ContainerView(OptionView):
    model = Container