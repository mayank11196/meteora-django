from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserSignupForm, UserLoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def signup(request):
	if request.method=='POST':
		data = request.POST
		user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'],
					first_name=data['first_name'], last_name=data['last_name'])
		return HttpResponse('Succesfully Registered')


	elif request.method=='GET':
		form = UserSignupForm()
		return render(request, 'register.html', {'r_form': form})

def signin(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponse('Logged-in Succesfully')
			else:
				return HttpResponse('Account is deactivated')

		else:
			return HttpResponse('Invalid login credentials')

	else:
		form = UserLoginForm()
		return render(request, 'login.html', {'l_form':form})