from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#  migration allows for the changes 
class Post(models.Model):
    title= models.CharField(max_length=100)
    content =models.TextField()
    date_posted =models.DateTimeField(default=timezone.now)
    author =models.ForeignKey(User, on_delete=models.CASCADE)
  # using foreign key because a single user can have multiple post and if a user is deleted the corresponding post is deleted as well

    def __str__(self):
        return self.title