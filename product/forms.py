from django import forms
from .models import Products 


class ProductForm(forms.Form):
	image = forms.ImageField(widget=forms.FileInput(attrs={
		"class": "img-upload"
		}))
	item_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
		"placeholder": "Item Name",
		"class": "form-control",
		"id":"name",
		}))
	item_status = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
		"placeholder": "Item Status",
		"class": "form-control",
		"id": "statusform"
		}))
	no_of_item = forms.IntegerField(widget=forms.NumberInput(attrs={
		"class": "form-control",
		"id": "item_no"
		}), min_value=0)
	Tax = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
		"placeholder": '99.99',
		"class": "form-control",
		"id" : "tax_form"
		}))
	Description = forms.CharField(required=False ,widget=forms.Textarea(attrs={
		"placeholder": 'Description',
		"class": "form-control",
		"id": "desc",
		}))
	Price = forms.DecimalField(widget=forms.NumberInput(attrs={
		"class": "form-control",
		"placeholder": "99.99",
		"id": "price",
		}), min_value=0)
	image1 = forms.ImageField(required=False)
	image2 = forms.ImageField(required=False)
	image3 = forms.ImageField(required=False)
	image4 = forms.ImageField(required=False)
	image5 = forms.ImageField(required=False)

			
			

