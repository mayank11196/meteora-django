from django.db import models

"""
This file contains the details about the users
"""

class User(models.Model):
	f_name = models.CharField(max_length=30)
	l_name = models.CharField(max_length=30)
	user_name = models.CharField(max_length=20)
	
