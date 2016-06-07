from django.contrib import admin
from .models import Order, Flavor, Topping, Container
#from .forms import FlavorForm, ToppingForm, ContainerForm

model_list = [Order, Flavor, Topping, Container]

admin.site.register(model_list)
