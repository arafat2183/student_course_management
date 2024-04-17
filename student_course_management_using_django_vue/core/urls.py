
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import studentView

urlpatterns = [
    path('api/', studentView),
]
