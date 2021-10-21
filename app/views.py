from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from app.form import KitchenForm
from app.models import Kitchen
from app.form import BeautyForm
from app.models import Beauty
from app.form import StationeryForm
from app.models import Stationery 
from app.models import Home
from app.form import HomeForm
from app.models import Food
from app.form import FoodForm
from app.models import Offer  
from app.form import OfferForm
from app.models import Loyal  
from app.form import LoyalForm
from app.models import Staff  
from app.form import StaffForm
from app.models import Order
from app.form import OrderForm
#from app.models import Domain  
#from app.form import DomainForm

from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from app.form import CreateUserForm

def home(request):
	return render(request,'home.html')

def home_cust(request):
	return render(request,'home_cust.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def access(request):
	return render(request,'access.html')

def kitchen(request):
	kit=Kitchen.objects.all()
	return render(request,'kitchen.html',{'kit':kit})

#add new kitchen
def addk(request):
	context={}

	form=KitchenForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/kitchen')

	context['form']=form
	return render(request,'add.html',context)

#add new beauty
def addb(request):
	context={}

	form=BeautyForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/beauty')

	context['form']=form
	return render(request,'add.html',context)

#add new stationery
def adds(request):
	context={}

	form=StationeryForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/stationery')

	context['form']=form
	return render(request,'add.html',context)

#add new homecare
def addh(request):
	context={}

	form=HomeForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/homecare')

	context['form']=form
	return render(request,'add.html',context)

#add new food
def addf(request):
	context={}

	form=FoodForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/food')

	context['form']=form
	return render(request,'add.html',context)


def beauty(request):
	bea=Beauty.objects.all()
	return render(request,'beauty.html',{'bea':bea})

def stationery(request):
	sta=Stationery.objects.all()
	return render(request,'stationery.html',{'sta':sta})

def food(request):
	foo=Food.objects.all()
	return render(request,'food.html',{'foo':foo})

def homecare(request):
	hom=Home.objects.all()
	return render(request,'homecare.html',{'hom':hom})

def offer_pg(request):
	off=Offer.objects.all()
	return render(request,'offer_pg.html',{'off':off})

def show_cust(request):
	cu=Loyal.objects.all()
	return render(request,'show_cust.html',{'cu':cu})

def staff_pg(request):
	stf=Staff.objects.all()
	return render(request,'staff_pg.html',{'stf':stf})

#updation & deletion for kitchenware
def kupdate(request,id):
	context={}
	kobj=get_object_or_404(Kitchen,id=id)

	form=KitchenForm(request.POST or None, instance=kobj)

	if form.is_valid():
		form.save()
		return redirect('/kitchen')

	context["form"]=form  

	return render(request,"update.html",context)

def kdelete(request,id):
	context={}

	obj=get_object_or_404(Kitchen,id=id)

	if request.method=='POST':
		obj.delete()
		return redirect('/to_order')

	return render(request,'kdelete.html')

#updation & deletion for beauty
def bupdate(request,id):
	context={}
	bobj=get_object_or_404(Beauty,id=id)

	form=BeautyForm(request.POST or None, instance=bobj)

	if form.is_valid():
		form.save()
		return redirect('/beauty')

	context["form"]=form  

	return render(request,"update.html",context)

def bdelete(request,id):
	context={}

	obj=get_object_or_404(Beauty,id=id)

	if request.method=='POST':
		obj.delete()
		return redirect('/to_order')

	return render(request,'bdelete.html')

#updation & deletion for stationery
def supdate(request,id):
	context={}
	sobj=get_object_or_404(Stationery,id=id)

	form=StationeryForm(request.POST or None, instance=sobj)

	if form.is_valid():
		form.save()
		return redirect('/stationery')

	context["form"]=form  

	return render(request,"update.html",context)

def sdelete(request,id):
	context={}

	obj=get_object_or_404(Stationery,id=id)

	if request.method=='POST':
		obj.delete()
		return redirect('/to_order')

	return render(request,'sdelete.html')

#updation & deletion for homecare
def hupdate(request,id):
	context={}
	hobj=get_object_or_404(Home,id=id)

	form=HomeForm(request.POST or None, instance=hobj)

	if form.is_valid():
		form.save()
		return redirect('/homecare')

	context["form"]=form  

	return render(request,"update.html",context)

def hdelete(request,id):
	context={}

	obj=get_object_or_404(Home,id=id)

	if request.method=='POST':
		obj.delete()
		return redirect('/to_order')

	return render(request,'hdelete.html')

#updation & deletion for food
def fupdate(request,id):
	context={}
	fobj=get_object_or_404(Food,id=id)

	form=FoodForm(request.POST or None, instance=fobj)

	if form.is_valid():
		form.save()
		return redirect('/food')

	context["form"]=form  

	return render(request,"update.html",context)

def fdelete(request,id):
	context={}

	obj=get_object_or_404(Food,id=id)

	if request.method=='POST':
		obj.delete()
		return redirect('/to_order')

	return render(request,'fdelete.html')


#loyalty customers
def lupdate(request,id):
	context={}
	lobj=get_object_or_404(Loyal,id=id)

	form=LoyalForm(request.POST or None, instance=lobj)

	if form.is_valid():
		form.save()
		return redirect('/show_cust')

	context["form"]=form  

	return render(request,"lupdate.html",context)



def odelete(request,id):
	context={}

	obj=get_object_or_404(Order,id=id)

	if request.method=='POST':
		obj.delete()
		return redirect('/show_order')

	return render(request,'odelete.html')

'''login and registration page'''

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form=CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
		context = {'form':form}
		return render(request, 'accounts/register.html', context)


def login(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				#login(request)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)


#updation & deletion for Staff in domains(association)
def stf_update(request,id):
	context={}
	obj=get_object_or_404(Staff,id=id)

	form=StaffForm(request.POST or None, instance=obj)

	if form.is_valid():
		form.save()
		return redirect('/staff_pg')

	context["form"]=form  

	return render(request,"stf_update.html",context)

def stf_delete(request,id):
	context={}

	obj=get_object_or_404(Staff,id=id)

	if request.method=='POST':
		obj.delete()
		return redirect('/staff_pg')

	return render(request,'stf_delete.html')

#add new STAFF
def add_stf(request):
	context={}

	form=StaffForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/staff_pg')

	context['form']=form
	return render(request,'add_stf.html',context)

#add new CUSTOMER
def add_cst(request):
	context={}

	form=LoyalForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/show_cust')

	context['form']=form
	return render(request,'add_cst.html',context)

#add new to_order form 
def to_order(request):
	context={}

	form=OrderForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/home')

	context['form']=form
	return render(request,'to_order.html',context)

#display table of order to be placed
def show_order(request):
	od=Order.objects.all()
	return render(request,'show_order.html',{'od':od})

#kitchen search
def ksearch(request):
    if request.method == "POST":
        query_name = request.POST.get('Name', None)
        if query_name:
            results = Kitchen.objects.filter(Name__contains=query_name)
            return render(request, 'ksearch.html', {"results":results})

    return render(request, 'ksearch.html')


#beauty search
def bsearch(request):
    if request.method == "POST":
        query_name = request.POST.get('Name', None)
        if query_name:
            results = Beauty.objects.filter(Name__contains=query_name)
            return render(request, 'bsearch.html', {"results":results})

    return render(request, 'bsearch.html')

#stationery search
def ssearch(request):
    if request.method == "POST":
        query_name = request.POST.get('Name', None)
        if query_name:
            results = Stationery.objects.filter(Name__contains=query_name)
            return render(request, 'ssearch.html', {"results":results})

    return render(request, 'ssearch.html')

#food search
def fsearch(request):
    if request.method == "POST":
        query_name = request.POST.get('Name', None)
        if query_name:
            results = Food.objects.filter(Name__contains=query_name)
            return render(request, 'fsearch.html', {"results":results})

    return render(request, 'fsearch.html')

#homecare search
def hsearch(request):
    if request.method == "POST":
        query_name = request.POST.get('Name', None)
        if query_name:
            results = Home.objects.filter(Name__contains=query_name)
            return render(request, 'hsearch.html', {"results":results})

    return render(request, 'hsearch.html')



def logout(request):
	#logout(request)
	return redirect('/')

def index(request):
	return render(request,'index.html')

