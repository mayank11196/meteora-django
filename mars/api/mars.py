import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz"

def curiosity():
	app_token = "DEMO_KEY"
	payload = {'api_key': app_token}

	response = requests.get(url, params=payload)

	return response.json()