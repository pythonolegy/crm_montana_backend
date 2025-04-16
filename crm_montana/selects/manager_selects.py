from crm_montana.models import Manager
from django.shortcuts import get_object_or_404

def get_department_by_id(manager_id):
    """Get Manager by id or 404, if it doesn't found"""
    return get_object_or_404(Manager, id=manager_id)

def list_departments(filters=None):
    """Get Managers list with filters"""
    if filters is None:
        filters = {}
    return Manager.objects.filter(**filters)
