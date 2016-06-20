<<<<<<< HEAD
from django.core.mail import send_mail
=======
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
>>>>>>> origin/master
from django.utils.timezone import now
from django.views import generic
from .models import Flavor, Topping, Container
from .forms import OrderForm

TYPE_TAGLINE_DICT = {
    'Flavor': 'Flavors to Savor',
    'Topping': "Poppin' Toppin's",
    'Container': 'No-Brainer Containers'
}


def get_topping_str(toppings):
    toppings_str = ''

    for topping in toppings:
        toppings_str += '{}, '.format(topping)
    toppings_str = toppings_str[:-2]

    return toppings_str


def get_email_context(order, toppings):
    context = {
        'name': order.name,
        'flavor': order.flavor,
        'toppings': toppings,
        'container': order.container,
    }
    return context


def send_email(to_list, subject, message, sender="claires.icecream.order@gmail.com"):
    msg = EmailMessage(subject, message, sender, to_list)
    msg.content_subtype = "html"
    return msg.send()


def email_to_customer(email, context):
    message = render_to_string('email_to_customer.html', context)
    send_email([email], 'Your Order', message)


def email_to_claire(context):
    message = render_to_string('email_to_claire.html', context)
    send_email(['meyer.alexander.john@gmail.com'], 'New Order', message)


class OrderView(generic.FormView):
    form_class = OrderForm
    success_url = 'success/'
    template_name = 'order.html'

    def form_valid(self, form):
        order = form.save(commit=False)
        order.order_time = now()
        order.save()

<<<<<<< HEAD
        body = make_order_body()

        claire_email_body = 'A new order for ice cream was made by ' + order.name + '.\n\n' + body
        send_mail('New Order',
                  claire_email_body,
                  'claires.icecream.order@gmail.com',
                  ['tech@mighty.com'],
                  fail_silently=False
                  )
=======
        toppings = form.cleaned_data.get('toppings')
        toppings = get_topping_str(toppings)
>>>>>>> origin/master

        email_context = get_email_context(order, toppings)
        email_to_customer(order.email, email_context)
        email_to_claire(email_context)

        return super().form_valid(form)


class OptionView(generic.ListView):
    template_name = 'choices.html'

    @property
    def get_type(self):
        return self.model.__name__

    @property
    def get_tagline(self):
        return TYPE_TAGLINE_DICT[self.get_type]

    def get_context_data(self, **kwargs):
        context = dict()
        context['option_type_cap'] = '{}s'.format(self.get_type)
        context['tagline'] = self.get_tagline
        context['option_list'] = self.get_queryset()

        return context


class FlavorView(OptionView):
    model = Flavor


class ToppingView(OptionView):
    model = Topping


class ContainerView(OptionView):
    model = Container