from django.contrib import admin
from .models import Category, Sub_Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Add the fields you want to display

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Add the fields you want to display

admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, SubCategoryAdmin)