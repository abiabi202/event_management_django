from django.db import models

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=20,default='')
    phone=models.IntegerField(null=True)
    email=models.CharField(max_length=30,default='')
    date=models.DateField(max_length=30,default='')
    place=models.CharField(max_length=30,default='')
    event=models.CharField(max_length=30,default='')
    image=models.ImageField(upload_to='sample/',null=True,blank=True)
    doc=models.FileField(upload_to='sample1/',null=True,blank=True)


class contact(models.Model):
    fname = models.CharField(max_length=20, default='')
    lname = models.CharField(max_length=20, default='')
    phone = models.BigIntegerField(null=True, blank=True)  
    email = models.EmailField(max_length=254, default='') 
    message = models.TextField(default='')  