from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import db

class home(ListView):
    model=db
    template_name='home.html'
    context_object_name='nigga'

