"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('home_cust',views.home_cust,name='home_cust'),
    
    path('about',views.about,name='about'),
    
    path('addk',views.addk,name='addk'),
    path('addb',views.addb,name='addb'),
    path('adds',views.adds,name='adds'),
    path('addh',views.addh,name='addh'),
    path('addf',views.addf,name='addf'),
    path('to_order',views.to_order,name='to_order'),
    #path('show_fp',views.show_fp,name='show_fp'),
    
    path('offer_pg',views.offer_pg,name='offer_pg'),
    path('show_cust',views.show_cust,name='show_cust'),
    path('show_order',views.show_order,name='show_order'),

    path('staff_pg',views.staff_pg,name='staff_pg'),
    path('stf_update/<id>',views.stf_update,name='stf_update'),
    path('stf_delete/<id>',views.stf_delete,name='stf_delete'),
    path('add_stf',views.add_stf,name='add_stf'),
    path('add_cst',views.add_cst,name='add_cst'),


    path('kupdate/<id>',views.kupdate,name='kupdate'),
    path('bupdate/<id>',views.bupdate,name='bupdate'),
    path('supdate/<id>',views.supdate,name='supdate'),
    path('lupdate/<id>',views.lupdate,name='lupdate'),
    path('hupdate/<id>',views.hupdate,name='hupdate'),
    path('fupdate/<id>',views.fupdate,name='fupdate'),
    
    path('kdelete/<id>',views.kdelete,name='kdelete'),
    path('bdelete/<id>',views.bdelete,name='bdelete'),
    path('sdelete/<id>',views.sdelete,name='sdelete'),
    path('hdelete/<id>',views.hdelete,name='hdelete'),
    path('fdelete/<id>',views.fdelete,name='fdelete'),
    path('odelete/<id>',views.odelete,name='odelete'),
     
    #path('admin/app/loyal/'),
    path('ksearch',views.ksearch,name='ksearch'),
    path('bsearch',views.bsearch,name='bsearch'),
    path('ssearch',views.ssearch,name='ssearch'),
    path('fsearch',views.fsearch,name='fsearch'),
    path('hsearch',views.hsearch,name='hsearch'),


    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),  
    path('logout/', views.logout, name="logout"),
    
    path('contact', views.contact, name="contact"),
    path('', views.index, name="index"),

    path('kitchen',views.kitchen,name='kitchen'),
    path('beauty',views.beauty,name='beauty'),
    path('homecare',views.homecare,name='homecare'),
    path('stationery',views.stationery,name='stationery'),
    path('food',views.food,name='food'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)