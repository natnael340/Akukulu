from django.contrib import admin
from .models import Products, Images, ProductHolder, TypeObject, Review, Reply
# Register your models here.

admin.site.register(Products)
admin.site.register(Images)
admin.site.register(ProductHolder)
admin.site.register(TypeObject)
admin.site.register(Review)
admin.site.register(Reply)