from django.conf.urls import url
from . import views

urlpatterns = [
			url(r'^$', views.query_search),
			url(r'result/', views.search_result)
		]