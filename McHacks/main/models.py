from django.db import models
import datetime

# Create your models here.
class Search(models.Model):
    userAddress = models.CharField(max_length=200)
    userConcern = models.CharField(max_length=200)
    timeStamp = datetime.datetime.now()
    
    def __init__(self):
    	super(Search, self).__init__()

    def __str__(self):
        return self.userAddress

def add_search_form_submission(Search):
	print("Hi Form Submitted.")
	# userAddress = request.POST['userAddress']
	# userConcern = request.POST['userConcern']
	timeStamp = datetime.datetime.now()
	search = Search(Search.userAddress, Search.userConcern)

	return(search, "main/dashboard.html")