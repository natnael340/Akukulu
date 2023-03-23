from django.urls import re_path
from . import views



urlpatterns = [
	re_path(r'^$',views.index, name='index'),
	re_path(r'^products/$',views.home, name='home'),
	re_path(r'^product/(?P<id>\d+)/$',views.item, name='item'),
	re_path(r'^addproduct/$', views.addproduct, name='addproduct'),
	
	]

