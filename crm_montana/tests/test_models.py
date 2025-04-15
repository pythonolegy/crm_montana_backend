import pytest
from crm_montana.models import Department, Manager, Employee, Client

@pytest.mark.django_db
def test_client_model():
    department = Department.objects.create(name="Sales", description="Sales Department")
    manager = Manager.objects.create(
        name="Alice",
        last_name="Smith",
        email="alies@test.test",
        phone="+1234567890",
        department=department
    )
    employee = Employee.objects.create(
        name="Bob",
        last_name="Johnson",
        email="bob@example.com",
        phone="+987654321",
        manager=manager,
        department=department,
        position="Sales Rep"
    )
    client = Client.objects.create(
        name="Test",
        last_name="Client",
        email="client@test.test",
        phone="0123456789",
        employee=employee,
    )
    assert str(client) == "Test Client"
    assert client.employee.name == "Bob"

@pytest.mark.django_db
def test_department_model():
    department = Department.objects.create(name="Sales", description="Sales Department")
    assert str(department.name) == "Sales"

@pytest.mark.django_db
def test_manager_model():
    department = Department.objects.create(name="Sales", description="Sales Department")
    manager = Manager.objects.create(
        name="Alice",
        last_name="Smith",
        email="alies@test.test",
        phone="+1234567890",
        department=department
    )
    assert str(manager) == "Alice Smith"
    assert manager.department.name == "Sales"

@pytest.mark.django_db
def test_employee_model():
    department = Department.objects.create(name="Sales", description="Sales Department")
    manager = Manager.objects.create(
        name="Alice",
        last_name="Smith",
        email="alies@test.test",
        phone="+1234567890",
        department=department
    )
    employee = Employee.objects.create(
        name="Bob",
        last_name="Johnson",
        email="bob@example.com",
        phone="+987654321",
        manager=manager,
        department=department,
        position="Sales Rep"
    )
    assert str(employee) == "Bob Johnson"
    assert employee.manager.name == "Alice"
    assert employee.manager.department.name == "Sales"

