from django.urls import path
from .views import SpotList, SpotDetail, SurfsessionDetail, SurfsessionList

urlpatterns = [
    path('spots/', SpotList.as_view(), name='spot-list'),
    path('spots/<int:pk>/', SpotDetail.as_view(), name='spot-detail'),
    path('surfsessions/', SurfsessionList.as_view(), name='surfsession-list'),
    path('surfsessions/<int:pk>/', SurfsessionDetail.as_view(), name='surfsession-detail'),
]