from django.urls import path, register_converter

from . import views
from .utils import HashIdConverter

register_converter(HashIdConverter, "hashid")

urlpatterns = [
  path('', views.MessageCreate.as_view(), name='index'),
  path('s/<hashid:pk>', views.MessageDetailView.as_view(), name='message-detail'),
]
