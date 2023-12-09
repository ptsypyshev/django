from django.urls import path
from .views import OrderedProducts

urlpatterns = [
    path('ordered-products/<int:customer_id>/', OrderedProducts.as_view(), name='ordered_products'),
]
