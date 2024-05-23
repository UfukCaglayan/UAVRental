from django.db import models
from django.shortcuts import redirect
from UAVRental import forms

# Veritabanındaki tablolara karşılık gelecek olan model classları yazılmıştır

# Marka bilgileri için model
class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name


# İHA modelleri için model (modeller markalara bağlıdır)
class Model(models.Model):
    model_id = models.AutoField(primary_key=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name


# Kategori bilgileri için model
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


# İHA bilgileri için model
class Uav(models.Model):
    uav_id = models.AutoField(primary_key=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_id = models.ForeignKey(Model, on_delete=models.CASCADE)
    weight = models.IntegerField()
    image = models.ImageField(upload_to="images", default="")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


# Kiralama kayıtları için model
class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    uav_id = models.ForeignKey(Uav, on_delete=models.CASCADE)
    customer_id = models.IntegerField()
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)


# İHA resimlerinin yüklenmesi
def upload(request):
    if request.method == "POST":
        form = forms.UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image=request.FILES["image"])
            model.save()
            return redirect('/')


class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")
