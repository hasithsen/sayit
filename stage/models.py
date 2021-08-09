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
  created_at = models.DateTimeField(auto_now_add=True)
  
  # class Meta:
  #     ordering = ['-id']

  def get_absolute_url(self):
    """Returns the url to access a particular instance of message."""
    return reverse('message-detail', args=[self.id])

  def __str__(self):
    """String for representing the messge object (in Admin site etc.)."""
    return f'{self.id} - {self.content}'
