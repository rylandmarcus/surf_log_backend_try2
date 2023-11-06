# users/serializers.py
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models
from surflog.serializers import SurfsessionSerializer

class UserCreateSerializer(UserCreateSerializer):
    surfsessions = SurfsessionSerializer(many=True, read_only=True)
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username', 'password', 'surfsessions')
