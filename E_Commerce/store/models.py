from django.db import models

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
    
class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
    name = models.CharField(max_length=150)
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    
    def __str__(self):
        return self.name