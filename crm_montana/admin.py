from django.contrib import admin
from .models import Manager, Department, Employee, Client, Deal, DealClient, Product, DealProduct, Category, \
    ProductCategory


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('name', 'created_at')
    search_fields = ('id', 'name', 'created_at')

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('name', 'last_name', 'created_at')
    search_fields = ('id', 'name', 'last_name', 'email', 'phone', 'created_at')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('name', 'last_name', 'created_at')
    search_fields = ('id', 'name', 'last_name', 'email', 'phone', 'created_at')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('name', 'last_name', 'created_at')
    search_fields = ('id', 'name', 'last_name', 'email', 'phone', 'created_at')

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('name', 'created_at')
    search_fields = ('id', 'name', 'created_at')

@admin.register(DealClient)
class DealClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'deal', 'client', 'added_at')
    list_filter = ('deal', 'client')
    search_fields = ('deal__name', 'client__name', 'client__last_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at')
    list_filter = ('name', 'price', 'created_at')
    search_fields = ('id', 'name', 'price', 'created_at')

@admin.register(DealProduct)
class DealProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'deal', 'quantity', 'price', 'added_at')
    list_filter = ('product', 'deal', 'quantity', 'price')
    search_fields = ('id', 'product__name', 'deal__name', 'quantity', 'price')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('name', 'created_at')
    search_fields = ('id', 'name', 'created_at')

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'category', 'added_at')
    list_filter = ('product', 'category')
    search_fields = ('id', 'product__name', 'category__name')