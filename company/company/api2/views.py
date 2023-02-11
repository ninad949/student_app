from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from api2.models import Employee
from api2.serializers import Employee
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee
