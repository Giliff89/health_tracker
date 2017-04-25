# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.views import generic
# from django.utils import timezone

# class IndexView(generic.ListView):
#     template_name = 'health_tracker/index.html'
#     context_object_name = 'health tracker overview'

from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the health tracker index.")
