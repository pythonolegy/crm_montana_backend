from rest_framework import viewsets
from crm_montana.models import Department, Manager, Client, Employee, Deal, DealClient

from .serializers import DepartmentSerializer, ManagerSerializer, ClientSerializer, EmployeeSerializer, DealSerializer, DealClientSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class DealClientViewSet(viewsets.ModelViewSet):
    queryset = DealClient.objects.all()
    serializer_class = DealClientSerializer
