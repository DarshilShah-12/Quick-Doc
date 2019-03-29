import requests

API_KEY = AIzaSyCauISu_jwPz5y4UwoVF7PcpYjuRvdCAFc

class HealthCareLocations()
""" Calculate the closest healthcare locations depending on the need specified in the user form"""

    def __init__(self, userAddress, userConcern)
        self.userAddress = userAddress
        self.userConcern = userConcern
        self.apiKey = API_KEY

    def getRequest(self, url, headers)
    """ General API get request function to be used when making the GCP API calls """
        return requests.request("GET", url, data=payload, headers=headers)

    def calcLocationCoordiantes(self)

        addr_tokens = split(self.userAddress, ",")
        
        parametersDict = {"base_https": "https://maps.googleapis.com/maps/api/geocode/", "mode": "json", 
                            "address": address}



