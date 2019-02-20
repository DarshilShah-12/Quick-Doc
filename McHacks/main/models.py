from django.db import models
import datetime

# Create your models here.
class Search(models.Model):
    address = models.CharField(max_length=200)
    search_for = models.CharField(max_length=200)
    submit_datetime = datetime.datetime.now()

    def __str__(self):
        return self.address