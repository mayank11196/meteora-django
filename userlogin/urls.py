from django.conf.urls import url
from . import views

urlpatterns = [	
				url(r'^login/$', views.login),
				url(r'^login/(?P<user_name>[a-z]{})/(?P<password>[a-z]{})/$', views.login),		
		]