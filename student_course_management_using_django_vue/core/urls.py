
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import StudentViewSet

router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')

urlpatterns = [
    path('api/', include(router.urls)),
]