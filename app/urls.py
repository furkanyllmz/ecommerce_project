from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),  # http://localhost:8000/
    path('products/', views.product_list, name='product_list'),
    path('products/<str:uid>/', views.product_detail, name='product_detail'),
    path('cart/',     views.cart,           name='cart'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)