from django.db import models

# Create your models here.
class Message_Model(models.Model):
    Name = models.CharField(max_length=150)
    Message  = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Name
