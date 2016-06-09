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
    flavor = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/flavors")

    def __str__(self):
        return u'{0}'.format(self.flavor)


class Topping(models.Model):
    topping = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/toppings")

    def __str__(self):
        return u'{0}'.format(self.topping)


class Container(models.Model):
    container = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/containers")

    def __str__(self):
        return u'{0}'.format(self.container)

