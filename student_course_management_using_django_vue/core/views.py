from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
