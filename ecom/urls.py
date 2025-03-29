from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product-detail/<int:product_id>', views.product_detail, name='product-detail'),
]