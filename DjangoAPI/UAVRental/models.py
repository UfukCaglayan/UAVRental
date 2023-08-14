from django.db import models
from django.db.models import Q
from UAVRental import forms
from django.shortcuts import redirect
from UAVRental.forms import UploadForm

#Veritabanındaki tablolara karşılık gelecek olan model classları yazılmıştır

#Marka bilgileri için model
class Brand(models.Model):
    BrandID = models.AutoField(primary_key=True)
    BrandName = models.CharField(max_length=50)

    def __str__(self):
        return self.BrandName

#İHA modelleri için model (modeller markalara bağlıdır)
class Model(models.Model):
    ModelID = models.AutoField(primary_key=True)
    BrandID = models.ForeignKey(Brand,on_delete=models.CASCADE)
    ModelName = models.CharField(max_length=50)

    def __str__(self):
        return self.ModelName
    
#Kategori bilgileri için model
class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.CategoryName
    
#Kategori bilgileri için model
class Uav(models.Model):
    UavID = models.AutoField(primary_key=True)
    BrandID = models.ForeignKey(Brand,on_delete=models.CASCADE)
    ModelID = models.ForeignKey(Model,on_delete=models.CASCADE)
    Weight = models.IntegerField()
    Image = models.ImageField(upload_to="images",default="")
    CategoryID = models.ForeignKey(Category,on_delete=models.CASCADE)

 #Kiralama kayıtları için model
class Rental(models.Model):
    RentalID = models.AutoField(primary_key=True)
    UavID =  models.ForeignKey(Uav,on_delete=models.CASCADE)
    CustomerID = models.IntegerField()
    BeginDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    Created = models.DateTimeField(auto_now_add=True)

#İHA resimlerinin yüklenmesi
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST,request.FILES)

        if(form.is_valid()):
            model = UploadModel(image = request.FILES["image"])
            model.save()
            return redirect('/')

class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")
