import requests


# initializing variable data
max_occupancy = 30


# cisco data from MV
ZONE = "0"
API_KEY = '45858da7ce53360c9999eb9131764963922fdfba'
CAMERA_SERIAL_NUM_1 = 'Q2FV-XEJ9-BTZG'
POSTMAN_TOKEN = '2fc76385-bf31-4798-9466-6f5087c85f7b'
url_1 = "https://n61.meraki.com/api/v0/devices/" + CAMERA_SERIAL_NUM_1 + "/camera/analytics/live"

def get_response(url):
    return requests.request("GET", url, data=payload, headers=headers)

def process_json(json):
    textDict = json
    # timestamp = textDict["ts"]
    zonesDict = textDict["zones"]
    personDict = zonesDict[ZONE]
    return personDict["person"]


payload = ""
headers = {
    'X-Cisco-Meraki-API-Key': API_KEY,
    'cache-control': "no-cache",
    'Postman-Token': POSTMAN_TOKEN
    }
    


# camera 1
response1 = get_response(url_1)
print(response1)
personNum1 = process_json(response1.json())
print("Camera one: {0}".format(personNum1))
