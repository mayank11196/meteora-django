from django import forms

class UserRegistrationForm(forms.Form):
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')
	username = forms.CharField(label='Username')
	email = forms.EmailField(label='Email')
	password = forms.CharField(label='Password')


class UserLoginForm(forms.Form):
	username = forms.CharField(label='Username')
	password = forms.CharField(label='Password')
