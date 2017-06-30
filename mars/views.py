from django.shortcuts import render
from .api import mars
from django.contrib.auth.models import User

def home(request):
	user = User.objects.get(id=request.user.id)
	username = user.username
	data = mars.curiosity()['photos'][0]

	rover = data['rover']
	rover_name = rover['name']
	launch_date = rover['launch_date']
	landing_date = rover['landing_date']

	camera = data['camera']
	camera_name = camera['name']
	camera_full_name = camera['full_name']

	image = data['img_src']
	

	context = {'image': image, 'rover_name': rover_name, 'launch_date': launch_date, 
			'landing_date': landing_date, 'camera_name': camera_name, 'camera_full_name': camera_full_name, 'username': username}
			
	return render(request, "mars.html", context)
	