import requests

API_KEY = AIzaSyCauISu_jwPz5y4UwoVF7PcpYjuRvdCAFc

class HealthCareLocations():
""" Calculate the closest healthcare locations depending on the need specified in the user form"""

    def __init__(self, userAddress, userConcern):
        self.userAddress = userAddress
        self.userConcern = userConcern
        self.apiKey = API_KEY

    def getRequest(self, url, headers):
    """ General API get request function to be used when making the GCP API calls """
        return requests.request("GET", url, data=payload, headers=headers)

    def emergencyPlaceSearch(self):


        coords = self.locationCoords.replace("(", "")
        coords = coords.replace(")", "")

        parDic = {"base_https": "https://maps.googleapis.com/maps/api/place/findplacefromtext/json", 
                            "point": coords, "radius": "2000", "input" = "hospitals", "fields" = 
                            ["formatted_address,name,opening_hours,rating"]}

        # format the url 
        url = "{0}?input={1}&inputtype=textquery&fields={2}&locationbias=circle:{3}@{4}&key={5}".format(
        parDic["base_https"],parDic["input"], parDic["fields"],parDic["radius"], parDic["point"], API_KEY)

        jsonOutput = getRequest(url)




