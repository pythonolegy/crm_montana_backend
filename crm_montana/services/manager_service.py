from crm_montana.models import Manager

def get_manager_data():
    return Manager.objects.prefetch_related('managers', 'employees')

def create_manager(**validated_data):
    return Manager.objects.create(**validated_data)

def update_manager(instance, **validated_data):
    for attr, value in validated_data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance