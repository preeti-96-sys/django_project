from django.contrib import admin
from .models import Loyal
from .models import Offer   
from .models import Domain  
from .models import Staff  
# Register your models here.
class LoyalAdmin(admin.ModelAdmin):
	list_display=['Name','Contact','Email','Last']

class OfferAdmin(admin.ModelAdmin):
	list_display=['Category','Name','Img','Valid']


class DomainAdmin(admin.ModelAdmin):
	list_display=['name','dom_id']

class StaffAdmin(admin.ModelAdmin):
	list_display=['s','name','gender']

admin.site.register(Offer,OfferAdmin)
admin.site.register(Loyal,LoyalAdmin)
admin.site.register(Domain,DomainAdmin)
admin.site.register(Staff,StaffAdmin)
