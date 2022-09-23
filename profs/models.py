from django.db import models
from django.contrib.auth.models import User
from product.models import Products 

class prof(models.Model):
    locs = (
        ('A.A', 'Addis Abeba'),
        ('HW', 'Hawassa'),
        ('B.D', 'Bahirdar'),
        ('D.D', 'Dire Dewa'),
        ('MK', 'Mekele'),
        ('JM', 'Jimma'),
        ('AS', 'Assosa'),
        ('HR', 'Harrar'),
        )
    user = models.OneToOneField(User, related_name='profs',on_delete=models.CASCADE)
    Fname = models.CharField(max_length=32, default="")
    Lname = models.CharField(max_length=32, default="")
    location = models.CharField(max_length=128, choices=locs)
    h_number = models.CharField(max_length=10, null=True)
    P_number = models.CharField(max_length=15, null=True)
    balance = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    
    
    def __str__(self):
        return self.Fname

class Transaction(models.Model):
	user = models.ForeignKey(prof, on_delete=models.CASCADE)	
	transactions = models.CharField(max_length=200)		
    
class favourite(models.Model):
	user = models.ForeignKey(prof, on_delete=models.CASCADE, null=True, blank=True)
	ip = models.CharField(max_length=32)
	favourite = models.ForeignKey(Products, on_delete=models.CASCADE)

		
User.profile = property(lambda u: prof.objects.get_or_create(user=u)[0])