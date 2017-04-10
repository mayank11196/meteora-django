from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .forms import QueryForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/register/login/')
def query_search(request):
	form = QueryForm()
	return render(request, 'query.html', {'form':form})


def api_request(payload):
	main_url = 'https://data.nasa.gov/resource/y77d-th95.json'

	app_token = None
	if app_token:
		header = {'Accept': 'application/json', 'X-App-Token': app_token}
	else:
		header = {'Accept': 'application/json'}

	response = requests.get(main_url, params=payload, headers=header)

	json_res = json.dumps(response.json(), indent=4)
	return json_res



def search_result(request):
	data = request.GET
	return HttpResponse(api_request(data))

