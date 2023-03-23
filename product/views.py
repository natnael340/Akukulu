from django.shortcuts import render, get_object_or_404
from .models import Products, Images, ProductHolder
from .forms import ProductForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from cart.models import Cart
from profs.models import favourite




def addproduct(request):
	
	myform = ProductForm()
	img = Images()
	user = User()
	if request.method == "POST":
		myform = ProductForm(request.POST, request.FILES or None)
		if myform.is_valid():
			print(myform.cleaned_data.keys())
			prod = Products.objects.create(item_name=myform.cleaned_data["item_name"], item_status="n_item", Tax=myform.cleaned_data["Tax"], 
				Description=myform.cleaned_data["Description"],Price=myform.cleaned_data["Price"], no_of_item=myform.cleaned_data["no_of_item"] )

			Images.objects.create(item=prod, image=myform.cleaned_data["image"])
			for i in myform.cleaned_data.keys():
				if i == "image":
					continue
				elif i.startswith("image") and myform.cleaned_data[i] != None:
					Images.objects.create(item=prod, image=myform.cleaned_data[i])
			ProductHolder.objects.create(user=request.user, product=prod)
		else:
			print(myform.errors)

	context = {
		"form": myform,
		"user": request.user
	}
	return render(request, 'productform.html', context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def index(request):
	
	if request.user.is_authenticated:
		fav = favourite.objects.filter(user = request.user.profs)
		context = {'product': Products.objects.all(), 'image': Images.objects.all(), 'fav': fav}
	else:
		print(str(request.META['REMOTE_ADDR']))
		fav = favourite.objects.filter(ip=str(request.META['REMOTE_ADDR']))
		context = {'product': Products.objects.all(), 'image': Images.objects.all(), 'fav': fav}
	if is_ajax(request):
		p = Products.objects.get(id=request.GET['id'])
		if not request.GET['cart']:
			data = set_fav(request, fav, p)
		else:
			data=set_cart(request, p)
		return JsonResponse(data)

		
	return render(request, 'home.html', context)
def home(request):
	if request.user.is_authenticated:
		fav = favourite.objects.filter(user = request.user.profs)
		context = {'product': Products.objects.all(), 'fav': fav}
	else:
		fav = favourite.objects.filter(ip=str(request.META['REMOTE_ADDR']))
		context = {'product': Products.objects.all(), 'fav': fav}
	dat = {}
	if is_ajax(request):
		if request.GET['type']:
			if request.GET['type']==1:
				prod =  Products.objects.all().order_by("item_name")
				for p in prod:
					pass 

		if request.method == 'POST':
			product = Products.objects.filter(item_name__contains=request.POST['text'])
			context = {
				"data": [],
			}
			for p in product:
				context["data"].append({
					'id': p.id,
					'itemName': p.item_name,
					'price': p.Price,
					'img': Images.objects.filter(item=p)[0].urls(),
				})
			return JsonResponse(context)
		else:
			data = del_cart(request)
			return JsonResponse(data)
	return render(request, 'index.html',context)

def item(request, id=None):
	instance = get_object_or_404(Products, pk=id)
	img_instance = Images.objects.filter(item=instance)
	context = {'product': instance, 'image': img_instance,}
	return render(request, 'product_info.html',context)

def del_cart(request):
	for i in range(int(request.GET["no"])):
		id = request.GET["id"][i]
		cart = Cart.objects.get(id=id)
		cart.delete()

	data = {
		'deleted': True,	
	}
	return data
def set_cart(request, p):
	cart = Cart.objects.create(
	user=(request.user if request.user.is_authenticated else None), 
			ip=str(request.META["REMOTE_ADDR"]), 
			product=p
		)
	data = {
		"cart": True,
		}
	return data

def set_fav(request, fav, p):
	try:
		fav = get_object_or_404(fav,favourite=p)
		fav.delete()
		data = {
			"fav": False,
			}
	except:
		favourite.objects.create(user=request.user.profs, ip=str(request.META["REMOTE_ADDR"]), favourite=p)
		data = {
			"fav": True,
			}
	return data