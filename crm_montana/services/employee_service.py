from crm_montana.models import Employee

def get_employee_data():
    return Employee.objects.prefetch_related('managers', 'employees')

def create_employee(**validated_data):
    return Employee.objects.create(**validated_data)

def update_employee(instance, **validated_data):
    for attr, value in validated_data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance