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
<<<<<<< HEAD
    # componentForm = models.ForeignKey(AddressComponents, on_delete = models.PROTECT)
=======
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
>>>>>>> 9be192228f7c40e84d71e03873c3946956fa8e7a
    timeStamp = datetime.datetime.now()
    
    def __init__(self):
    	super(Search, self).__init__()

    def __str__(self):
<<<<<<< HEAD
        return self.userAddress





# def add_search_form_submission(Search):
# 	print("Hi Form Submitted.")
# 	# userAddress = request.POST['userAddress']
# 	# userConcern = request.POST['userConcern']
# 	timeStamp = datetime.datetime.now()
# 	search = Search(Search.userAddress, Search.userConcern)

# 	return(search, "main/dashboard.html")
=======
        return self.userAddress
>>>>>>> 9be192228f7c40e84d71e03873c3946956fa8e7a
