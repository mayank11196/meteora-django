from django.shortcuts import render
from .models import User


def login(request):
	data = request.POST
	user = User(f_name=data['first_name'], l_name=data['last_name'], user_name=data['username'])
	user.save()
	return render(request, 'userprofile.html', {'user_name':data['first_name']})
	