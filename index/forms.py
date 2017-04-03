from django import forms

class UserForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	username = forms.CharField()
	#email_addr = forms.EmailField()
