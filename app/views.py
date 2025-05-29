from django.shortcuts import render
from pymongo import MongoClient
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def product_list(request):
    client = MongoClient(settings.MONGO_URI)
    db = client['ecommerce']
    collection = db['products']
    products = list(collection.find())

    # Her ürüne image_url ekle (eğer image varsa)
    for p in products:
        p['image_url'] = p.get('image', '')

    return render(request, 'product_list.html', {'products': products})

def product_detail(request, uid):
    client = MongoClient(settings.MONGO_URI)
    db = client['ecommerce']
    collection = db['products']
    product = collection.find_one({'uid': uid})
    if product:
        product['image_url'] = product.get('image', '')
    return render(request, 'detail.html', {'product': product})

def cart(request):
    return render(request, 'cart.html')
