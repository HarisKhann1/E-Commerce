from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    #  Foreign key to Category model to create a relationship between Category and Sub_Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Product(models.Model):

    stocks = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    )

    image = models.ImageField(upload_to='product_images/')
    name = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)   
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, default=1)
    stock = models.CharField(max_length=50, choices=stocks, default='Available', null=True,)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField(default=0)
    address = models.TextField()
    phone = models.CharField(max_length=11)
    date = models.DateField(auto_now_add=True)

