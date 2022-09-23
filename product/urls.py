from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^products/$',views.home, name='home'),
	url(r'^product/(?P<id>\d+)/$',views.item, name='item'),
	url(r'^addproduct/$', views.addproduct, name='addproduct'),
	
	]

