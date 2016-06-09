from django.contrib import admin
from .models import Order, Flavor, Topping, Container


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'flavor', 'order_time')
    list_filter = ['order_time', 'name', 'flavor']


class FlavorAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'image')


class ToppingAdmin(admin.ModelAdmin):
    list_display = ('topping', 'image')


class ContainerAdmin(admin.ModelAdmin):
    list_display = ('container', 'image')

admin.site.register(Order, OrderAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Container, ContainerAdmin)
