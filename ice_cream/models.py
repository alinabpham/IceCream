from __future__ import unicode_literals
from django.db import models
from django import forms
from django.contrib import admin


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


class Flavor(models.Model):
    flavors = models.CharField(max_length=50)

    def __str__(self):
        return u'{0}'.format(self.flavors)


class Topping(models.Model):
    toppings = models.CharField(max_length=50)

    def __str__(self):
        return u'{0}'.format(self.toppings)


class Container(models.Model):
    containers = models.CharField(max_length=50)

    def __str__(self):
        return u'{0}'.format(self.containers)


class Image(models.Model):
    pass