# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Drink, Food, Activity

admin.site.register(Drink)
admin.site.register(Food)
admin.site.register(Activity)
