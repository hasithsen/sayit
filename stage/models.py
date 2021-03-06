from django.db import models
from django.urls import reverse  


class Message(models.Model):
  """Model representing a message."""
  sender = models.CharField(
    max_length=200,
    null=True, 
    blank=True,
    # help_text="Enter name of sayer"
    ) 
  receiver = models.CharField(
    max_length=200,
    null=True, 
    blank=True,
    # help_text="Enter name of sayee"
    ) 
  content = models.CharField(
    max_length=500,
    null=True, 
    blank=False,
    # help_text="Enter content to say"
    ) 
  views = models.IntegerField(
    default=0,
    null=True, 
    blank=False,
    # help_text="Number of views"
    )
  created_at = models.DateTimeField(auto_now_add=True)
  
  # class Meta:
  #     ordering = ['-id']

  def _get_views(self):
    """Returns the value of views attribute of the message instance"""
    return self.views

  def get_absolute_url(self):
    """Returns the url to access a particular instance of message."""
    return reverse('message-detail', args=[self.id])

  def __str__(self):
    """String for representing the messge object (in Admin site etc.)."""
    return f'{self.id} - {self.content} - {self.views}'
