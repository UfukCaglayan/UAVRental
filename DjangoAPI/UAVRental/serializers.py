from rest_framework import serializers
from UAVRental.models import Uav,Rental,Brand,Model,Category

class UavSerializer(serializers.UavSerializer):
    class Meta:
        model = Uav
        fields = ('UavID','BrandID','ModelID','Weight','Image','CategoryID')

class BrandSerializer(serializers.BrandSerializer):
    class Meta:
        model = Brand
        fields = ('BrandID','BrandName')

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('ModelID','BrandID','ModelName')

class CategorySerializer(serializers.CategorySerializer):
    class Meta:
        model = Category
        fields = ('CategoryID','CategoryName')


class RentalSerializer(serializers.RentalSerializer):
    class Meta:
        model = Rental
        fields = ('RentalID','UavID','CustomerID','BeginDate','EndDate','Created')



