from django.template import Library
import math

register = Library() 


@register.filter(name='money')
def money(value):
	value=str(value)
	print(value)
	try:
		value, dec = value.split(".")
	except :
		value=value
		dec = "00"
	
	for i in range(1,math.ceil(len(value)/3)):
		value = value[:-3*(i)]+","+value[-3*(i):]
	return value+"."+dec

@register.filter(name='multiply')
def multiply(value):
	try:
		return float(value)*0.15
	except Exception as e:
		return 0.0

@register.filter(name='favp')
def favp(value, prod):
	try:
		v = value.get(favourite = prod)
		print(str(v))
		return str(v)
	except:
		return ""
	
@register.filter(name='imgf')
def imgf(value):
	return value[1:]

@register.filter(name='birr')
def birr(value, i):
	v = str(value)
	v=v.split(".")
	return v[i];


@register.filter(name='tax')
def tax(value):
	v = float(value)
	if v>0:
		return "Tax inclusive ("+value+"%)"
	else:
		return "Tax Exclusive"