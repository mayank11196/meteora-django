from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegistrationForm, UserLoginForm

def index(request):
	
	return render(request, 'index.html')
