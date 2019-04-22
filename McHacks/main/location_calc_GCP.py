import requests
import googlemaps

API_KEY = "AIzaSyCauISu_jwPz5y4UwoVF7PcpYjuRvdCAFc"

class HealthCareLocations():

    def __init__(self, userAddress, userConcern, latitude, longitude):
        self.userAddress = userAddress
        self.userConcern = userConcern
        self.latitude    = latitude
        self.longitude   = longitude
        self.apiKey = API_KEY


    def emergencyPlaceSearch(self):

        gmaps = googlemaps.Client(key=self.apiKey)
        location = [self.latitude, self.longitude]
        radius = 20000
        placesResult = gmaps.places(query="hospitals", location=location, radius=radius)['results']
        return placesResult

if __name__ == '__main__':

    search = HealthCareLocations("", "", 43.4643, -80.5204)
    place = search.emergencyPlaceSearch()
    print("place: ", place)






