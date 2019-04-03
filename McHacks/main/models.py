from django.db import models
import datetime

USER_CONCERNS = (
    ('emergency','EMERGENCY'),
)

# Create your models here.
class Search(models.Model):
    userAddress = models.CharField(max_length=200)
    userConcern = models.CharField(max_length=9, choices=USER_CONCERNS, default="emergency")
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    timeStamp = datetime.datetime.now()
    
    def __init__(self):
    	super(Search, self).__init__()

    def __str__(self):
        return self.userAddress