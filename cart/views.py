from django.shortcuts import render
from .models import Cart, Orderd
from product.models import Products, Images, ProductHolder
from django.http import JsonResponse
# Create your views here.

def cart_view(request):
	print(str(request.META['REMOTE_ADDR']))
	if request.is_ajax():
		p = Products.objects.get(id=request.GET['id'])
		k = p.Price
		print("price", k)
		if request.user.is_authenticated:
			ca = Cart.objects.get(user=request.user, product=p)
		else:
			ca = Cart.objects.get(ip=str(request.META['REMOTE_ADDR']), product=p) 
		ca.delete()
		data = {
			'deleted': True,
			

		}
		return JsonResponse(data)

	
	try:
		if request.user.is_authenticated:
			prod = Cart.objects.filter(user=request.user)	
			context = {
			"products" : prod,
			}
		else:
			prod = Cart.objects.filter(ip=str(request.META['REMOTE_ADDR']))
			context = {
			"products" : prod,
			}
		return render(request, 'cart.html', context)
	except Exception as e:
		print(e)
		context = {
			"products": None,
		}
		return render(request, 'cart.html', context)	
	

