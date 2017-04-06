from django import forms

class QueryForm(forms.Form):
	name = forms.CharField(label="Name of the meteorite")
	mass = forms.IntegerField(label="Mass of the meteorite in kgs")
	recclass = forms.CharField(label="Class of the meteorite", max_length=2)
