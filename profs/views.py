from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lgn
from .forms import User, CreateUser
from product.views import home
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache
from product.models import ProductHolder, Images

@never_cache
def index(request):
	if not request.user.is_authenticated:
		return redirect('signin')
	context = {'user': request.user, 'prods': []}
	prods = ProductHolder.objects.filter(user = request.user)
	for p in prods:
		context['prods'].append({'product':p.product, 'img': Images.objects.get(item=p.product)})
	print(context)

	return render(request, 'account.html', context)
def login(request):
	userform = User()
	context = {
	"form": userform,
	} 
	print(userform)
	if request.method == "POST":
		userform = User(request.POST)
		if userform.is_valid():
			user = authenticate(username=userform.cleaned_data["username"], password=userform.cleaned_data["password"])
			if user is not None:
				lgn(request, user)
				return redirect("index")
			else:
				context["N_logged"]=True
		else:
			print(userform.errors)


		
	return render(request, 'account_signin.html', context)

	def signup(request):
		userform = CreateUser()
		context = {
		"form": userform,
		}

	return render(request, 'account_signin.html', context)
