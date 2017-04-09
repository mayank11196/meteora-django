from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserSignupForm


def signup(request):
	if request.method=='POST':
		data = request.POST
		user = User(username=data['username'], email=data['email'], password=data['password'])
		user.save()
		return redirect('/search')


	elif request.method=='GET':
		form = UserSignupForm()
		return render(request, 'register.html', {'r_form': form})

