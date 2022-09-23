from django.db import models
from PIL import Image
import os
from django.contrib.auth.models import User
from django.conf import settings
from .backend import predict

# Create your models here.
class Products(models.Model):
	status = (
		('New','New'),
		('Used','Used'),
		('Slightly Used','Slightly Used'),)
	catagories = (
			('Electronics & Office', 'Electronical & Office'),
			('Cloth', 'Cloth'),
			('Jewellery', 'Jewellery'),
			('Games & Programs','Games & Programs'),
			('Beauty & Health','Beauty & Health'),
			('Automotives & Industrial', 'Automotives & Industrial'),
			('Others', 'Others'),
		)
	item_name = models.CharField(max_length=32)
	item_status = models.CharField(max_length=32, choices=status)
	Tax = models.CharField(max_length=32)
	Description = models.TextField(blank=True, null=True)
	Price = models.DecimalField(max_digits=10, decimal_places=2)
	discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	P_date = models.DateTimeField(auto_now_add=True)
	catagory = models.CharField(max_length=32, choices=catagories, null=True)
	rate = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
	no_of_item = models.IntegerField(default=0)
	sold = models.IntegerField(default=0)

	def delete(self, *args, **kwargs):
		img = Images.objects.filter(item=self)
		if img:
			for i in img:
				print(i)
				i.delete()

		super(Products, self).delete(*args, **kwargs)

	def __str__(self):
		return self.item_name



class Images(models.Model):
	item = models.ForeignKey(Products, on_delete=models.CASCADE)
	image = models.ImageField()

	def url(self):
		a = '/' + '/'.join(self.image.path.split("/")[-2:])
		im = ''.join(a.split(".")[:-1]) + '.png'
		im = im[:-3]+'png'
		return im
	def post_save(self, *args, **kwargs):
		super().save()
		print("here it saves")
	def pre_save(self, *args, **kwargs):
		super().save()
		print("here it saves pre")
	def save(self, *args, **kwargs):
		print(self.image.path)
		super().save()
		b_w=300
		b_h=300
		img = Image.open(self.image.path)
		w,h = img.size
		if w>h:
			h = round(b_w*(h/w))
			w=b_w
		else:
			w = round(b_h*(w/h))
			h=b_h
		img = img.resize((w,h), Image.ANTIALIAS)
		background = Image.new('RGBA', (b_w,b_h), (255,255,255,0))
		offset = ((b_w-w)//2,(b_h-h)//2)
		background.paste(img,offset)
		print(background.size)
		print(''.join(self.image.path.split(".")[:-1]) + '.png')	
		os.remove(self.image.path)
		background.save(''.join(self.image.path.split(".")[:-1]) + '.png')
		print(self.image.path)

	def delete(self, *args, **kwargs):
		print("called")
		super(Images, self).delete(*args, **kwargs)
		img = self.image
		try:
			if os.path.isfile(img.path):
				os.remove(img.path)
		except Exception  as e:
			print(e)
			

		super(Images, self).delete(*args, **kwargs)
	
	def __str__(self):
		return str(self.id)	



class ProductHolder(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	product = models.OneToOneField(Products, on_delete=models.CASCADE)


class Review(models.Model):
	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	comment = models.TextField()
	c_date = models.DateTimeField(auto_now_add=True)

	

	def save(self, *args, **kwargs):
		prevcount = Review.objects.all().count()
		super().save()
		val = 1
		rate = self.product.rate
		if(rate!=0.0):
			val = self.predict()
			print(rate)
			value = (float(rate)/5.0)*prevcount
			value += val
			val = value/Review.objects.all().count()

		self.product.rate = val*5.0
		self.product.save(update_fields=['rate',])

	

	def __str__(self):
		return self.product.item_name + " - "+ self.user.username

class Reply(models.Model):
	product = models.ForeignKey(Review, on_delete=models.CASCADE)
	reply = models.TextField()

	def __str__(self):
		return self.pk

class TypeObject(models.Model):
	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	title = models.CharField(max_length=32)
	object_type = models.CharField(max_length=32)
	no = models.PositiveIntegerField() 
		

		
		
		


		