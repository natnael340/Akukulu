from django.urls import re_path
from . import views

urlpatterns = [
	re_path(r'^signin/',views.login, name='signin'),
	re_path(r'^',views.index, name='account'),
	]