# # import requests
# from django.db import models
# API_KEY = "AIzaSyCauISu_jwPz5y4UwoVF7PcpYjuRvdCAFc"

# """ Calculate the closest healthcare locations depending on the need specified in the user form"""
# class HealthCareLocations():
#     def __init__(self, locationCoords):
#         # self.userAddress = userAddress
#         # self.userConcern = userConcern
#         self.locationCoords = locationCoords
#         self.apiKey = API_KEY

#     """ General API get request function to be used when making the GCP API calls"""
#     def getRequest(self, url, headers):
#         return requests.request("GET", url, data=payload, headers=headers)

#     def calcLocationCoordiantes(self):

#         addr_tokens = split(self.userAddress, ",")
        
#         parametersDict = {"base_https": "https://maps.googleapis.com/maps/api/geocode/", "mode": "json", 
#                             "address": address}



