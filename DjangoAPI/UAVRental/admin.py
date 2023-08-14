from django.contrib import admin
from UAVRental.models import Uav,Brand,Model,Category

admin.site.register(Uav)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Category)

# Oluşturulan modellerin admin paneline eklenmesiyle beraber kayıt ekleme,silme ve güncelleme işlemler yapılabilmektedir.
