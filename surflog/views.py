from django.shortcuts import render
from rest_framework import generics
from .models import Surfsession, Spot
from .serializers import SpotSerializer, SurfsessionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .helpers import GetBody
from users.models import User
# Create your views here.

class SpotList(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

class SpotDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

class SurfsessionList(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Surfsession.objects.all()
    serializer_class = SurfsessionSerializer
    def get(self, request, *args, **kwargs):
        queryset = Surfsession.objects.filter(user = request.user.id)
        serializer = SurfsessionSerializer(queryset, many=True)
        # return Response(request.user.id)
        return Response(serializer.data)
    def post(self, request):
        body = GetBody(request)
        print(body)
        print(request.user.id)
        spot_id = body["spot"]
        user_id = request.user.id  
        spot = Spot.objects.get(pk=spot_id)
        user = User.objects.get(pk=user_id)
        queryset = Surfsession.objects.create(notes=body["notes"], board=body["board"], size=body["size"], spot=spot, user=user)
        serializer = SurfsessionSerializer(queryset)
        return Response(serializer.data)

class SurfsessionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Surfsession.objects.all()
    serializer_class = SurfsessionSerializer

