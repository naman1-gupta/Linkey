from django.shortcuts import render
from django.views.generic import ListView
from .models import Link, Vote

class LinkListView(ListView):
    model = Link
    template_name = 'linkey/links.html'
    context_object_name = 'links'