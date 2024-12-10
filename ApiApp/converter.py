from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):  # Use ModelSerializer for ease of use
    class Meta:
        model = Student
        fields = '__all__'  # Automatically includes all fields in the model