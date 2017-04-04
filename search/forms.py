from django import forms

class QueryForm(forms.Form):
	name = forms.CharField(label="Name of the meteorite")