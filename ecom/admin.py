from django.contrib import admin
from .models import Category, Product

class AdminCategories(admin.ModelAdmin):
    list_display = ('name', 'created_at')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'created_at')

admin.site.register(Category, AdminCategories)
admin.site.register(Product, AdminProduct)
