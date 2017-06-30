import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY"

def curiosity():

	response = requests.get(url)

	return response.json()