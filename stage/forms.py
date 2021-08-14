from django.forms import ModelForm, TextInput, Textarea
from .models import Message


class MessageCreateForm(ModelForm):
  class Meta:
    model = Message
    fields = ['content', 'sender', 'receiver']
    # initial = {'content': 'Your say here'}
    widgets = {
      'sender': TextInput(attrs={'placeholder': 'Enter name of sayer'}),
      'receiver': TextInput(attrs={'placeholder': 'Enter name of sayee'}),
      'content': Textarea(attrs={'placeholder': 'Enter content to say', 'rows': 5}),
    }
    labels = {
      'sender': 'Said by (optional)',
      'receiver': 'Said to (optional)',
      'content': 'Message',
    }

  def __init__(self, *args, **kwargs):
    super(MessageCreateForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-control shadow'
