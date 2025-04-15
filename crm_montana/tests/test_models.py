from django.test import TestCase

from crm_montana.models import Department, Manager, Employee


class ModelsTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(
            name="Sales", description="Sales Department"
        )
        self.manager = Manager.objects.create(
            name="Alice",
            last_name="Smith",
            email="alies@test.test",
            phone="+1234567890",
            department=self.department,
        )
        self.employee = Employee.objects.create(
            name="Bob",
            last_name="Johnson",
            email="bob@example.com",
            phone="+987654321",
            manager=self.manager,
            department=self.department,
            position="Sales Rep"
        )

    def test_department_model(self):
        self.assertEqual(str(self.department.name), "Sales")

    def manager_model(self):
        self.assertEqual(str(self.manager), "Alice Smith")
        self.assertEqual(self.manager.department.name, "Sales")

    def employee_model(self):
        self.assertEqual(str(self.employee), "Bob Johnson")
        self.assertEqual(self.employee.manager.name, "Alice")
        self.assertEqual(self.employee.manager.department.name, "Sales")

