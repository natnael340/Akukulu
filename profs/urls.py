from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signin/',views.login, name='signin'),
	url(r'^',views.index, name='account'),
	]