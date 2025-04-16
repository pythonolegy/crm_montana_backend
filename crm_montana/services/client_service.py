from crm_montana.models import Client

def get_client_data():
    return Client.objects.prefetch_related('managers', 'employees')

def create_client(**validated_data):
    return Client.objects.create(**validated_data)

def update_client(instance, **validated_data):
    for attr, value in validated_data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance