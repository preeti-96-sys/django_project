from django import forms
from app.models import Kitchen
from app.models import Beauty
from app.models import Stationery
from app.models import Home
from app.models import Food
from app.models import Offer   
from app.models import Loyal  
from app.models import Staff
from app.models import Order
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  

class KitchenForm(forms.ModelForm):
	class Meta:
		model = Kitchen
		fields = "__all__"

class BeautyForm(forms.ModelForm):
	class Meta:
		model = Beauty
		fields = "__all__"

class StationeryForm(forms.ModelForm):
	class Meta:
		model = Stationery 
		fields = "__all__"

class HomeForm(forms.ModelForm):
	class Meta:
		model = Home
		fields = "__all__"

class FoodForm(forms.ModelForm):
	class Meta:
		model = Food
		fields ="__all__"

class LoyalForm(forms.ModelForm):
	class Meta:
		model= Loyal  
		fields = "__all__"

class OfferForm(forms.ModelForm):
	class Meta:
		model = Offer
		fields = "__all__"

class CreateUserForm(UserCreationForm):
	class Meta:
		model=User 
		fields=['username','email','password1','password2']

class StaffForm(forms.ModelForm):
	class Meta:
		model=Staff  
		fields="__all__"

class OrderForm(forms.ModelForm):
	class Meta:
		model=Order  
		fields="__all__"