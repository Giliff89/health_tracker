# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Drink(models.Model):
    drink_type = models.CharField(max_length=50)  # drink name
    drink_size = models.IntegerField(default=0)  # in ounces
    drink_calories = models.IntegerField(default=0)  # estimated calories, if applicable
    date_added = models.DateTimeField('date added')

    def __str__(self):
        return self.drink_type


@python_2_unicode_compatible
class Food(models.Model):
    food_type = models.CharField(max_length=100)  # food name
    food_calories = models.IntegerField(default=0)  # estimated calorie count
    date_added = models.DateTimeField('date added')

    def __str__(self):
        return self.food_type


@python_2_unicode_compatible
class Activity(models.Model):
    activity_type = models.CharField(max_length=50)  # name of activity
    activity_time = models.IntegerField(default=0)  # minutes of activity
    activity_distance = models.FloatField(default=0.0)  # if applicable, how many miles
    date_added = models.DateTimeField('date added')

    def __str__(self):
        return self.activity_type
