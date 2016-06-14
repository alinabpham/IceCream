from django.core.mail import send_mail
from django.utils.timezone import now
from django.views import generic
from .models import Option
from .forms import OrderForm

TYPE_TAGLINE_DICT = {
    'flavors': 'Flavors to Savor',
    'toppings': "Poppin' Toppin's",
    'containers': 'No-Brainer Containers'
}


class OrderView(generic.FormView):
    form_class = OrderForm
    success_url = 'success/'
    template_name = 'ice_cream/order.html'

    def form_valid(self, form):

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

        order = form.save(commit=False)
        order.order_time = now()
        order.toppings = get_topping_str()
        order.save()

        body = make_order_body()

        claire_email_body = 'A new order for ice cream was made by ' + order.name + '.\n\n' + body
        send_mail('New Order',
                  claire_email_body,
                  'claires.icecream.order@gmail.com',
                  ['tech@mighty.com'],
                  fail_silently=False
                  )

        customer_email_body = order.name + ',\n\n' + "Thank you for ordering from Claire's Creamery! Your order " + \
                              "details are as follows:" + '\n\n' + body + '\n\n' + "Let us " + \
                              "know if there are any issues, but mostly, enjoy that ice " + \
                              "cream!\n\nYour sweet tooth savior,\nClaire's Creamery"
        send_mail('Your Order',
                  customer_email_body,
                  'claires.icecream.order@gmail.com',
                  [order.email],
                  fail_silently=False
                  )

        return super(OrderView, self).form_valid(form)


class OptionView(generic.ListView):
    template_name = 'ice_cream/choices.html'
    model = Option

    @property
    def get_type(self):
        return str(self.kwargs.get('option_type'))

    @property
    def get_filter_type(self):
        # URL is plural
        return self.get_type[:-1]

    @property
    def get_tagline(self):
        return TYPE_TAGLINE_DICT[self.get_type]

    def get_queryset(self):
        return Option.objects.filter(group=self.get_filter_type)

    def get_context_data(self, **kwargs):
        context = dict()
        context['option_type_cap'] = self.get_type.capitalize()
        context['tagline'] = self.get_tagline
        context['option_list'] = self.get_queryset()

        return context