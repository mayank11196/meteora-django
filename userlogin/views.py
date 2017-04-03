from django.shortcuts import render


def login(request, user_name=None, password=None):
	
	return render(request, 'userlogin.html', {'user_name':user_name, 'password':password})