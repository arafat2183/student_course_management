from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['id', 'name', 'course', 'email', 'gender']
        fields = '__all__'