from crm_montana.models import Employee
from django.shortcuts import get_object_or_404

def get_department_by_id(employee_id):
    """Get Department by id or 404, if it doesn't found"""
    return get_object_or_404(Employee, id=employee_id)

def list_departments(filters=None):
    """Get Departments list with filters"""
    if filters is None:
        filters = {}
    return Employee.objects.filter(**filters)
