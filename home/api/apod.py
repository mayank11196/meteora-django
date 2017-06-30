import requests


url = "https://api.nasa.gov/planetary/apod"

def image():


	app_token = "DEMO_KEY"
	payload = {'api_key': app_token}

	header = {'Accept': 'application/json', 'X-App-Token': app_token}

	response = requests.get(url, params=payload)

	return response.json()
