from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # http://localhost:8000/
    path('products/', views.product_list, name='product_list'),
    
]