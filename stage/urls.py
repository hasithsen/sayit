from django.urls import path
from . import views

urlpatterns = [
  path('', views.MessageCreate.as_view(), name='index'),
  path('s/<int:pk>', views.MessageDetailView.as_view(), name='message-detail'),
]
