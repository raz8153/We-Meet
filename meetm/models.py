from django.db import models
# from django.utils import timezones
from django.contrib.auth.models import User

class Meetups(models.Model):
    # No = models.IntegerField()
    City = models.CharField(max_length=100)
    Venue = models.TextField()
    Time = models.TextField()
    Theme = models.TextField()
    MOderator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name