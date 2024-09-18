from django.db import models

# Create your models here.
class categoryDb(models.Model):
    categoryname = models.CharField(max_length=100, null=True, blank=True)
    category_image = models.ImageField(upload_to="categoryimages",null=True, blank=True)
class VehicleDb(models.Model):
    VehicleName = models.CharField(max_length=100, null=True, blank=True)
    BrandName = models.CharField(max_length=100, null=True, blank=True)
    VehicleType = models.CharField(max_length=100, null=True, blank=True)
    VehiclePrice = models.IntegerField(null=True, blank=True)
    VehicleImage = models.ImageField(upload_to="categoryimages", null=True, blank=True)
    Enginecapacity = models.CharField(max_length=100, null=True, blank=True)
    Mileage = models.CharField(max_length=100, null=True, blank=True)
    Fuelcapacity = models.CharField(max_length=100, null=True, blank=True)
    Maxpower = models.CharField(max_length=100, null=True, blank=True)



