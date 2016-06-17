from django.contrib import admin
from .models import Order, Flavor, Topping, Container

options = [Flavor, Topping, Container]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'flavor', 'order_time')
    list_filter = ['order_time', 'name', 'flavor']


class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


admin.site.register(Order, OrderAdmin)
admin.site.register(options, OptionAdmin)



