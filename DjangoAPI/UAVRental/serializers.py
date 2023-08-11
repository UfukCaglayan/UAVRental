from rest_framework import serializers
from UAVRental.models import Uavs,Rental

class UavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uavs
        fields = ('UavID','Brand','Model','Weight','Image','CategoryID')

class RentalSerializer(serializers.RentalSerializer):
    class Meta:
        model = Rental
        fields = ('RentalID','UavID','CustomerID','BeginDate','EndDate','Created')



