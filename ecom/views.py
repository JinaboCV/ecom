from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'ecom/index.html', context=context)

