from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .api import apod

def register(request):
	if request.method=='POST':
		email = request.POST.get('email')
		username = request.POST.get('username')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if password2==password1:
			user = User.objects.create_user(username=username, email=email, password=password1)
			user = authenticate(username=username, password=password1)

			if user:
				if user.is_active:
					login(request, user)
				else:
					return HttpResponse("User Not Active")
			else:
				return HttpResponse("User Not Registered")
			return redirect("/home/")

	return render(request, "register.html")

def login_view(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return redirect("/home/")
			else:
				return HttpResponse("User Not Active")
		else:
			return HttpResponse("Username or Password Not Correct")

	return render(request, "login.html")

@login_required
def home(request):
	user = request.user
	userdetails = User.objects.get(id=user.id)
	username = userdetails.username
	data = apod.image()
	img = data['hdurl']
	title = data['title']
	explanation = data['explanation']
	copyright = data['copyright']
	context = {"img": img, 'title': title, 'explanation': explanation, 'copyright': copyright, 'username': username}
	return render(request, "apod.html", context)

@login_required
def logout_view(request):
	logout(request)
	return redirect("/home/login/")