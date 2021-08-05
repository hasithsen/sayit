from django.shortcuts import render, get_object_or_404
from django.views import generic
# from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Message
from .forms import MessageCreateForm


class MessageCreate(generic.CreateView):
  model = Message
  form_class = MessageCreateForm


class MessageDetailView(generic.DetailView):
  model = Message
  context_object_name = 'message'
