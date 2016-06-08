from django.contrib import admin
from .models import Order, Flavor, Topping, Container

model_list = [Flavor, Topping, Container]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_time', 'name', 'flavor')
    list_filter = ['order_time', 'name', 'flavor']

admin.site.register(Order, OrderAdmin)
admin.site.register(model_list)
