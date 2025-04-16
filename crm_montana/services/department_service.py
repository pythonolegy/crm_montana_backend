from crm_montana.models import Department

def create_department(**data):
    return Department.objects.create(**data)

def update_department(instance, **data):
    for attr, value in data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance