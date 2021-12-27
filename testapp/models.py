from django.db import models

# Create your models here.
class Chats(models.Model):
    chats = models.CharField(max_length=250, blank=True, null=True,)