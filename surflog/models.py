from django.db import models
from users.models import User

# Create your models here.
class Spot(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Surfsession(models.Model):
    notes = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='surfsessions')
    size = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='surfsessions')

    def __str__(self):
        return self.name
