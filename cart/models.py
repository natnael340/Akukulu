from django.db import models
from product.models import Products
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	ip = models.CharField(max_length=20)
	product = models.ForeignKey(Products, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.ip)

class Orderd(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	d_place = models.CharField(max_length=264)
	o_date = models.DateTimeField(auto_now_add=True)
	d_date = models.DateTimeField()

	def __str__(self):
		return str(self.id)

		



		

