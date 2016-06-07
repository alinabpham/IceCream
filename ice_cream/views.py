from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import OrderForm
import datetime
from .models import Flavor, Topping, Container


def home_page(request):
        return render(request, 'ice_cream/home_page.html', {})


def OrderView(request):
    """
    template_name = 'order.html'
    form_class = OrderForm
    success_url = '/thanks/'

    """
    if request.method == "POST":
        form = OrderForm(request.POST)

    #there may be some sort of errors attribute or raise error method for redirecting

        if form.is_valid():
            order = form.save(commit=False)
            order.order_time = datetime.datetime.now()
            order.save()
            # ONCE ORDERED, SHOULD REDIRECT TO ANOTHER PAGE
            return redirect('/order/success')
        else:
            # Should maybe stay at the same page, with some error message? Compromise on this
            form = OrderForm()
    else:
        form = OrderForm()

    """
    def form_valid(self, form):
        form.send_email
        return super(OrderView, self).form_valid(form)
    """

    return render(request, 'ice_cream/order.html', {'form': form})


def OptionView(request, option_type):

    type_model_dict = {
        'flavors': Flavor,
        'toppings': Topping,
        'containers': Container,
    }

    def get_img_dict(option_list):
        img_dict = dict()

        for option in option_list:
            pass

    option_list = type_model_dict(option_type).objects.all()
    option_img_dict = get_img_dict(option_list)

    context = {'option_list': option_list, 'image_dict': option_img_dict}
    #how to make this path just choices?
    return render(request, 'ice_cream/choices.html', context)
