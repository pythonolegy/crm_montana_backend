from crm_montana.models import Client
from django.shortcuts import get_object_or_404

def get_department_by_id(client_id):
    """Get Department by id or 404, if it doesn't found"""
    return get_object_or_404(Client, id=client_id)

def list_departments(filters=None):
    """Get Departments list with filters"""
    if filters is None:
        filters = {}
    return Client.objects.filter(**filters)
