# company/api/serializers.py

from rest_framework import serializers
from api2.models import Employee
class Serializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
