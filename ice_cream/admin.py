from django.contrib import admin
from .models import Order, Flavor, Topping, Container


model_list = [Topping, Container]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'flavor', 'order_time')
    list_filter = ['order_time', 'name', 'flavor']


"""
class FlavorImageInline(admin.TabularInline):
    model = FlavorImage
"""


class FlavorAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'image')


admin.site.register(Order, OrderAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(model_list)
