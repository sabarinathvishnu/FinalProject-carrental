from django.db import models

# Create your models here.
class Contactdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)

class Bookingdb(models.Model):
    carname = models.CharField(max_length=100, null=True,blank=True)
    username = models.CharField(max_length=100, null=True,blank=True)
    
    brandname = models.CharField(max_length=100, null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    vehicletype = models.CharField(max_length=100, null=True,blank=True)
    pickuptime = models.TimeField(max_length=100, null=True,blank=True)
    pickofftime = models.TimeField(max_length=100, null=True,blank=True)
    pickuplocation = models.CharField(max_length=100, null=True,blank=True)
    dropofflocation = models.CharField(max_length=100, null=True,blank=True)
    pickupdate = models.DateField(max_length=100, null=True,blank=True)
    dropoffdate = models.DateField(max_length=100, null=True,blank=True)
    phonenumber = models.IntegerField(null=True,blank=True)

class signupdb(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    emailaddress = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    confirmpassword = models.CharField(max_length=100,null=True,blank=True)

class product(models.Model):
    title = models.CharField(max_length=100)
    qty = models.IntegerField()

    def __str__(self):
        return self.title
