from rest_framework import serializers
from crm_montana.models import Department, Manager, Client, Employee
from crm_montana.services.department_service import create_department, update_department
from crm_montana.services.manager_service import create_manager, update_manager
from crm_montana.services.client_service import create_client, update_client
from crm_montana.services.employee_service import create_employee, update_employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def create(self, validated_data):
        return create_department(**validated_data)

    def update(self, instance, validated_data):
        return update_department(instance, **validated_data)

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

    def create(self, validated_data):
        return create_manager(**validated_data)

    def update(self, instance, validated_data):
        return update_manager(instance, **validated_data)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        return create_client(**validated_data)

    def update(self, instance, validated_data):
        return update_client(instance, **validated_data)

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        return create_employee(**validated_data)

    def update(self, instance, validated_data):
        return update_employee(instance, **validated_data)