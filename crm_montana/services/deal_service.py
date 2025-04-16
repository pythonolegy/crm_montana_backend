from crm_montana.models import Deal

def get_deal_data():
    return Deal.objects.prefetch_related()

def create_deal(**validated_data):
    return Deal.objects.create(**validated_data)

def update_deal(instance, **validated_data):
    for attr, value in validated_data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance