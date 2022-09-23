from django import forms


class User(forms.Form):
	username = forms.CharField(max_length=64, widget=forms.TextInput(attrs={
		"class": "form-control userc",
		"placeholder": "Username",
		}))
	password = forms.CharField(max_length=64, widget=forms.PasswordInput(attrs={
		"class": "form-control userc",
		"placeholder": "Password",
		}))
class CreateUser(forms.Form):
	Fname = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
		"class": "form-control userc",
		"placeholder": "Abebe",
		}))
	Lname = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
		"class": "form-control userc",
		"placeholder": "Hailu",
		}))
	email = forms.EmailField(widget=forms.TextInput(attrs={
		"class": "form-control userc",
		"placeholder": "abebeH@mail.com",
		}))
	username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
		"class": "form-control userc",
		"placeholder": "abebe12",
		}))
	pasword = forms.CharField(max_length=32, widget=forms.PasswordInput())
	cpasword = forms.CharField(max_length=32, widget=forms.PasswordInput())
	location = forms.CharField(max_length=32)