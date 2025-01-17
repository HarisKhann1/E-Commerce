from django.contrib import admin
from .models import Category, Sub_Category, Product, Contact, Order

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Add the fields you want to display

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'date', 'category', 'sub_category', 'image')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','product', 'quantity', 'price', 'address', 'phone', 'date', 'total')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Order, OrderAdmin)