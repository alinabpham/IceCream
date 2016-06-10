from django.test import TestCase
from .forms import OrderForm
from .models import Flavor, Container, Topping, Order
from django.contrib.auth.models import User
from django.utils.timezone import now


# models test
class FlavorTest(TestCase):

    def create_flavor(self, flavor='Yum', image='images/flavors/Screen_Shot_2016-06-08_at_5.02.32_PM_ioctmW7.png'):
        return Flavor.objects.create(flavor=flavor, image=image)

    def test_flavor_creation(self):
        flav = self.create_flavor()
        self.assertTrue(isinstance(flav, Flavor))

    def create_wrong_flavor(self, flavor='Yum', image='images/flavors/Screen_Shot_2016-06-08_at_5.02.32_PM_ioctmW7.png'):
        return Flavor.objects.create(flavor)


class OrderTest(TestCase):

    def test_order_is_valid(self):
        flavor = Flavor.objects.create(flavor='Yum', image='images/flavors/Screen_Shot_2016-06-08_at_5.02.32_PM_ioctmW7.png')
        container = Container.objects.create(container='cup', image='images/containers/Screen_Shot_2016-06-08_at_5.02.32_PM_ioctmW7.png')
        topping = Topping.objects.create(topping='oreos', image='images/toppings/Screen_Shot_2016-06-08_at_5.02.32_PM_ioctmW7.png')

        order = Order.objects.create(flavor=flavor, container=container, toppings=topping, name='j', address='j',
                                     phone='j', email='meyer.alexander.john@gmail.com', order_time=now())
        self.assertTrue(isinstance(order, Order))


class OrderFormTest(TestCase):

    def test_order_form_is_valid(self):
        flavor = Flavor.objects.create(flavor='Yum',
                                       image='images/flavors/Screen_Shot_2016-06-08_at_5.02.32_PM_ioctmW7.png')
        container = Container.objects.create(container='cup',
                                             image='images/containers/Screen_Shot_2016-06-08_at_5.02.32_PM_ioctmW7.png')
        topping = Topping.objects.create(topping='oreos',
                                         image='images/toppings/Screen_Shot_2016-06-08_at_5.02.32_PM_ioctmW7.png')

        order_data = {
            'flavor': flavor,
            'toppings': topping,
            'container': container,
            'name': 'j',
            'address': 'j',
            'phone': 'j',
            'email': 'meyer.alexander.john@gmail.com',
        }

        order = OrderForm(data=order_data)
        self.assertTrue(isinstance(order, OrderForm))