from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import OrderForm
import datetime


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