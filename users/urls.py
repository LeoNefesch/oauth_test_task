from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<pk>/', UserDetails.as_view(), name='user-detail'),
    path('profile/', profile_view, name='profile'),
]
