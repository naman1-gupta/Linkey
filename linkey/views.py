from django.shortcuts import render
from django.views.generic import ListView
from .models import Link, Vote

class LinkListView(ListView):
    template_name = 'linkey/links.html'
    model = Link
    context_object_name = 'links'
    queryset = Link.with_votes.all()