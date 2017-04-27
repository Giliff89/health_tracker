# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Drink(models.Model):
    drink_type = models.CharField(max_length=50)  # drink name
    drink_size = models.IntegerField(default=0)  # in ounces
    drink_calories = models.IntegerField(default=0)  # estimated calories, if applicable


class Food(models.Model):
    food_type = models.CharField(max_length=100)  # food name
    food_calories = models.IntegerField(default=0)  # estimated calorie count


class Activity(models.Model):
    activity_type = models.CharField(max_length=50)  # name of activity
    activity_time = models.IntegerField(default=0)  # minutes of activity
    activity_distance = models.FloatField(default=0.0)  # if applicable, how many miles
