from django.shortcuts import render
from .forms import UserRegistrationForm, UserLoginForm

def index(request):
	l_form = UserLoginForm()
	r_form = UserRegistrationForm()
	return render(request, 'index.html', {'l_form':l_form, 'r_form':r_form})
	