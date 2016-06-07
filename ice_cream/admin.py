from django.contrib import admin
from .models import Order, Flavor, Topping, Container
#from .models import Flavor, Topping, Container

model_list = [Order, Flavor, Topping, Container]

admin.site.register(model_list)
