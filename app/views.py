from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):



    return render(request, 'index.html')


def product_list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'product_list.html', {'products': products})

# app/views.py

from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail(request, uid):
    # burada uid alanına göre ürünü alıyoruz
    product = get_object_or_404(Product, uid=uid)
    return render(request, 'detail.html', {
        'product': product
    })


from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, uid):
    product = get_object_or_404(Product, uid=uid)
    return render(request, 'detail.html', {'product': product})

def cart(request):
    # Sepet tümüyle JS ile yönetildiği için sadece boş bir sayfa render ediyoruz.
    return render(request, 'cart.html')
