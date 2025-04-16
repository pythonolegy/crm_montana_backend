from crm_montana.models import DealClient


def create_deal_client(deal, client):
    return DealClient.objects.create(deal=deal, client=client)


def update_deal_client(instance, deal, client):
    instance.deal = deal
    instance.client = client
    instance.save()
    return instance
