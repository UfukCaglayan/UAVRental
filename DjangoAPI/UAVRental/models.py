from django.db import models
 
# Create your models here.

class Uavs(models.Model):
    UavID = models.AutoField(primary_key=True)
    Brand = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Weight = models.IntegerField()
    Image = models.CharField(max_length=50)
    CategoryID = models.IntegerField()
     
    class Meta:  
        db_table = "Uavs"
        app_label = ''
     
    def __str__(self):
        return self


class Rental(models.Model):
    RentalID = models.AutoField(primary_key=True)
    UavID = models.IntegerField()
    CustomerID = models.IntegerField()
    BeginDate = models.DateTimeField(auto_now=True)
    EndDate = models.DateTimeField(auto_now=True)
    Created = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self
 
    class Meta:
        ordering = ['created']
         
    class Meta:  
        db_table = "Rentals"
        app_label = ''

class MyRental(models.Model):
    UavInfo= models.ForeignKey('UAVRental.Uavs',on_delete=models.CASCADE)  
    RentalInfo=  models.ForeignKey('UAVRental.Rental',on_delete=models.CASCADE)  