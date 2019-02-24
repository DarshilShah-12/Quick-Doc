from django.db import models
import datetime

# Create your models here.
class Search(models.Model):
    userAddress = models.CharField(max_length=200)
    userConcern = models.CharField(max_length=200)
    timeStamp = datetime.datetime.now()
    userConcernsList = ["Emergency", "Walk-In"]
    def __str__(self):
        return self.address