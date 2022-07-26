from django.forms import ModelForm
from .models import Message_Model

class message_form(ModelForm):   
    class Meta:
        model = Message_Model
        fields = ("Name", "Message")
