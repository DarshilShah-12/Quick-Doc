from django.db import models
import datetime

USER_CONCERNS = (
    ('emergency','EMERGENCY'),
)

# class AddressComponents(models.Model):
# 	street_number = models.CharField(max_length=200)
# 	route = models.CharField(max_length=200)
# 	locality = models.CharField(max_length=200)
# 	administrative_area_level_1 = models.CharField(max_length=200)
# 	country = models.CharField(max_length=200)
# 	postal_code = models.CharField(max_length=200)

# 	def __init__(self):
# 		super(AddressComponents, self).__init__()

# 	def __str__(self):
# 		return self.postal_code


# Create your models here.
class Search(models.Model):
    userAddress = models.CharField(max_length=200)
    userConcern = models.CharField(max_length=9, choices=USER_CONCERNS, default="emergency")
    longitude = models.DecimalField(max_digits=18, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=8, blank=True, null=True)
    timeStamp = datetime.datetime.now()
    
    def __init__(self):
    	super(Search, self).__init__()

    def __str__(self):
        return self.userAddress
