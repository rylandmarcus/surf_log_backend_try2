from rest_framework import serializers
from .models import Spot, Surfsession

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = '__all__'

class SurfsessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surfsession
        fields = '__all__'

