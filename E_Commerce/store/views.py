from django.shortcuts import render
from .models import Category, Sub_Category

# Create your views here.
def categories():
    categories = Category.objects.all()
    sub_categories = Sub_Category.objects.all()
    
    return {
        'categories': categories,
        'sub_categories': sub_categories
    }

def index(request):
    context = categories()
    return render(request, 'index.html', context)
