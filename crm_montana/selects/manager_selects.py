from crm_montana.models import Manager
from django.shortcuts import get_object_or_404

def get_department_by_id(manager_id):
    return get_object_or_404(Manager, id=manager_id)

def list_departments(filters=None):
    if filters is None:
        filters = {}
    return Manager.objects.filter(**filters)
