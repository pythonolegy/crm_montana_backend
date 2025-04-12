from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Manager(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    image_url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='managers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Employee(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=24)
    email = models.EmailField(unique=True)
    manager=models.ForeignKey(Manager,on_delete=models.CASCADE, related_name='employees')
    department_pk=models.ForeignKey(Department,on_delete=models.CASCADE, related_name='employees')
    position = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'