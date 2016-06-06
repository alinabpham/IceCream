from django.contrib import admin
from .models import Order, Option
from .forms import OptionForm

class OptionFormAdmin(admin.ModelAdmin):
    fields = ('flavors', 'toppings', 'containers',)
    list_display = ('flavors', 'toppings', 'containers',)
    form = OptionForm

admin.site.register(Order)
admin.site.register(Option, OptionFormAdmin)