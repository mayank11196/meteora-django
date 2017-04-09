from django import forms

class UserSignupForm(forms.Form):
	username = forms.CharField(label="Username")
	email = forms.EmailField(label="Email")
	password = forms.CharField(label="Password")

