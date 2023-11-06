# users/urls.py
from django.urls import path, include
from users import views
from .views import UserList

urlpatterns = [
  path('', include('djoser.urls')),
  path('', include('djoser.urls.authtoken')),
  path('users/', UserList.as_view(), name='user-list')
]