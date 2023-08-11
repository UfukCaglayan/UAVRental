from rest_framework import serializers
from UAVRental.models import Uavs

class UavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uavs
        fields = ('UavID','Brand','Model','Weight','Image','CategoryID')




