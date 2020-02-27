from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
      
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    contact = models.CharField(max_length=80 ,null=True)
    
    
    def __str__(self):
            return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()