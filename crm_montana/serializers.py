from rest_framework import serializers
from crm_montana.models import Department, Manager, Client, Employee, Deal, DealClient, Product, DealProduct
from crm_montana.services.department_service import create_department, update_department
from crm_montana.services.manager_service import create_manager, update_manager
from crm_montana.services.client_service import create_client, update_client
from crm_montana.services.employee_service import create_employee, update_employee
from crm_montana.services.deal_service import create_deal, update_deal
from crm_montana.services.deal_client_service import create_deal_client, update_deal_client
from crm_montana.services.product_service import create_product, update_product
from crm_montana.services.deal_product_service import create_deal_product, update_deal_product


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


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'

    def create(self, validated_data):
        return create_deal(**validated_data)

    def update(self, instance, validated_data):
        return update_deal(instance, **validated_data)


class DealClientSerializer(serializers.ModelSerializer):
    deal = serializers.PrimaryKeyRelatedField(queryset=Deal.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = DealClient
        fields = '__all__'

    def create(self, validated_data):
        return create_deal_client(**validated_data)

    def update(self, instance, validated_data):
        return update_deal_client(instance, **validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return create_product(**validated_data)

    def update(self, instance, validated_data):
        return update_product(instance, **validated_data)


class DealProductSerializer(serializers.ModelSerializer):
    deal = serializers.PrimaryKeyRelatedField(queryset=Deal.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = DealProduct
        fields = '__all__'

    def create(self, validated_data):
        return create_deal_product(**validated_data)

    def update(self, instance, validated_data):
        return update_deal_product(instance, **validated_data)
