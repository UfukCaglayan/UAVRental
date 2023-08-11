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

