from distutils.command.upload import upload
import email
from email.policy import default
from operator import mod
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class UserProfile(models.Model):
#       # user=models.OneToOneField(User,on_delete=models.CASCADE)
#       email=models.CharField(max_length=30,blank=True)
#       username=models.CharField(max_length=15,blank=False)
#       phone=models.CharField(max_length=10,blank=True)
#       gender=models.CharField(max_length=15,default='female')
     
class User1(models.Model):
    #   username=models.OneToOneField(User, on_delete=models.CASCADE)
    #   user = models.OneToOneField( User,on_delete=models.CASCADE)
      username=models.TextField(max_length=20)
      email=models.CharField(max_length=30,blank=True)
      phone=models.CharField(max_length=12,blank=True)
      gender=models.CharField(max_length=15,default='female')
      password=models.CharField(max_length=100)

class UserReg(models.Model):
      user = models.OneToOneField( User,on_delete=models.CASCADE)
      phone=models.CharField(max_length=12,blank=True)
      gender=models.CharField(max_length=15,default='female')
      user_type=models.CharField(max_length=10,blank=True)

class Category(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)
    price=models.CharField(max_length=100)
    cloth_image = models.ImageField(upload_to='images',default="/home/ts/Documents/j/demo_ecomm/ecomm/ecommerce/static/ecommerce/images/home/product1.jpg")  

class All_Category(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)
    price=models.CharField(max_length=100)
    cloth_image = models.ImageField(upload_to='images',default="/images/girl1.jpg")  
    category_type=models.TextField(max_length=50)


class Item(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)
    price=models.CharField(max_length=100)
    item_category=models.TextField(max_length=50)
    item_image=models.ImageField(upload_to='images',default="/images/girl1.jpg")

class MyCategory(models.Model):
    category=models.CharField(max_length=20)

class MyItem(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)
    price=models.FloatField(max_length=100)
    # item_category =models.TextField(max_length=50)
    item_image=models.ImageField(upload_to='images',default="/images/girl1.jpg")
    item_category= models.ForeignKey(MyCategory, null=True, on_delete=models.CASCADE)
      
class Add_Cart(models.Model):
    title= models.ForeignKey(MyItem, null=True, on_delete=models.CASCADE)   
    user= models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True,default=1)


def __str__(self):  
        return self.user.username