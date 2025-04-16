from crm_montana.models import Department
from django.shortcuts import get_object_or_404

def get_department_by_id(department_id):
    """Get Department by id or 404, if it doesn't found"""
    return get_object_or_404(Department, id=department_id)

def list_departments(filters=None):
    """Get Departments list with filters"""
    if filters is None:
        filters = {}
    return Department.objects.filter(**filters)
