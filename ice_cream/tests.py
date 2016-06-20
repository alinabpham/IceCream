from django.test import TestCase
from .forms import OrderForm
from .models import Option, Order
from django.utils.timezone import now

# TESTS ARE DEFUNCT, MUST CHANGE

# models test
class OptionTest(TestCase):

    def create_option(self, flavor='Yum', image='images/flavors/Screen_Shot_2016-06-08_at_5.02.32_PM_ioctmW7.png'):
        return Option.objects.create(group=flavor, image=image)

    def test_flavor_creation(self):
        flav = self.create_option()
        self.assertTrue(isinstance(flav, Option))

    def create_wrong_option(self, flavor='Yum', image='images/flavors/Screen_Shot_2016-06-08_at_5.02.32_PM_ioctmW7.png'):
        return Option.objects.create(flavor)


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