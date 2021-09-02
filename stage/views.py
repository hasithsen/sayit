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

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    self.object.views += 1
    self.object.save() 
    context = self.get_context_data(object=self.object)
    return self.render_to_response(context)
