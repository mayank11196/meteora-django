from django.conf.urls import url
from . import views

urlpatterns = [	
				url(r'^login/$', views.signin),
				url(r'^signup/$', views.signup),
			]