from crm_montana.models import Product

def get_product_data():
    return Product.objects.all()

def create_product(**validated_data):
    return Product.objects.create(**validated_data)

def update_product(instance, validated_data):
    for attr, value in validated_data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance

