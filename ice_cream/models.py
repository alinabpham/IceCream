from __future__ import unicode_literals
from django.db import models
from django import forms
from django.contrib import admin

OPTION_CHOICES = (
    ('flavor', 'Flavor'),
    ('topping', 'Topping'),
    ('container', 'Container'),
)


class Order(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    flavor = models.CharField(max_length=50)
    toppings = models.CharField(max_length=500)
    container = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    order_time = models.DateTimeField(blank=True)

    def __str__(self):
        return 'Order date: ' + str(self.order_time)


class Option(models.Model):
    group = models.CharField(max_length=50, choices=OPTION_CHOICES)
    option = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/options")

    def __str__(self):
        return u'{0}'.format(self.option)
