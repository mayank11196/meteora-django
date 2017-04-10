from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [	
				url(r'^login/$', auth_views.login,
					{'template_name': '/home/darkknight/Desktop/django_project/meteora-django/userlogin/templates/login.html'}),
				url(r'^signup/$', views.signup),
			]