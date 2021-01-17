from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class Message(models.Model):
    from_username = models.CharField(max_length=200)
    to_username = models.CharField(max_length=200)
    message = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    username= models.CharField(max_length=200)
    friends=models.ManyToManyField(User, blank=True)
    
class Discussion(models.Model):
    user1= models.ForeignKey(User, blank=True, related_name='person1', on_delete=models.CASCADE)
    user2= models.ForeignKey(User, blank=True, related_name='person2', on_delete=models.CASCADE)
    chats = models.ManyToManyField(Message, blank=True)