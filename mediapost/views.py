from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView
from wiki.forms import PageForm
from django.urls import reverse_lazy
from wiki.models import Page

# Create your views here.
class PostsForFeedListView(CreateView):
