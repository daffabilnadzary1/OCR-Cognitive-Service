from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('success/', success, name='success')
]