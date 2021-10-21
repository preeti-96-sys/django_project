from django.db import models

# Create your models here.
class Kitchen(models.Model):
	Name=models.CharField(max_length=50)
	Price=models.IntegerField()
	Company=models.CharField(max_length=40)

class Beauty(models.Model):
	Name=models.CharField(max_length=50)
	Price=models.IntegerField()
	Company=models.CharField(max_length=40)

class Stationery(models.Model):
	Name=models.CharField(max_length=50)
	Price=models.IntegerField()

class Home(models.Model):
	Name=models.CharField(max_length=50)
	Price=models.IntegerField()
	Company=models.CharField(max_length=40) 	

class Food(models.Model):
	Name=models.CharField(max_length=50)
	Price=models.IntegerField()

class Loyal(models.Model):
	Name=models.CharField(max_length=50)
	Contact=models.CharField(max_length=14)
	Email=models.CharField(max_length=50)  
	Last=models.DateField(auto_now=True)
	
class Offer(models.Model):
	Category=models.CharField(max_length=50)
	Name=models.CharField(max_length=500)
	Img=models.ImageField(upload_to="media")
	Valid=models.DateField(auto_now=False)

class Domain(models.Model):
	name=models.CharField(max_length=50)
	dom_id=models.CharField(max_length=10)

	def __str__(self):
		ret=self.name+','+self.dom_id
		return ret 

class Staff(models.Model):
	s=models.ForeignKey(Domain,on_delete=models.CASCADE)
	name=models.CharField(max_length=50)
	gender=models.CharField(max_length=10)


class Order(models.Model):
	product=models.CharField(max_length=50)
	placed=models.DateField(auto_now=True)