from django import forms

class UserSignupForm(forms.Form):
	first_name = forms.CharField(max_length=128, label="First Name")
	last_name = forms.CharField(max_length=128, label="Last Name")
	username = forms.CharField(max_length=128, label="Username")
	email = forms.EmailField(label="Email")
	password = forms.CharField(max_length=128, label="Password")


class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=128, label="Username")
	password = forms.CharField(max_length=128, label="Password")

