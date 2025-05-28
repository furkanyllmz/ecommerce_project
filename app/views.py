from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):



    return render(request, 'index.html')


def product_list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'product_list.html', {'products': products})
