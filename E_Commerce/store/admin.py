from django.contrib import admin
from .models import Category, Sub_Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Add the fields you want to display

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)