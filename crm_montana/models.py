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
    department=models.ForeignKey(Department,on_delete=models.CASCADE, related_name='employees')
    position = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Client(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=24)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE, related_name='clients')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Deal(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DealClient(models.Model):
    deal=models.ForeignKey(Deal,on_delete=models.CASCADE, related_name='clients')
    client=models.ForeignKey(Client,on_delete=models.CASCADE, related_name='deals')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('deal','client')

    def __str__(self):
        return f'{self.deal} - {self.client}'

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DealProduct(models.Model):
    deal=models.ForeignKey(Deal,on_delete=models.CASCADE, related_name='products')
    product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='deals')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('deal','product')

    def __str__(self):
        return f'{self.deal} - {self.product}'

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_categories')
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='product_categories')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product','category')

    def __str__(self):
        return f'{self.product} - {self.category}'