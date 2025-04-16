from crm_montana.models import DealProduct


def create_deal_product(deal, product, quantity, price):
    return DealProduct.objects.create(deal=deal, product=product, quantity=quantity, price=price)


def update_deal_product(instance, deal, product, quantity, price):
    instance.deal = deal
    instance.product = product
    instance.quantity = quantity
    instance.price = price
    instance.save()
    return instance
