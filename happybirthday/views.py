# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
def home(request, name):
    return render_to_response(name+'.html')