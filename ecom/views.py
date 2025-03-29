from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        products = Product.objects.filter(title__icontains = item_name)
    paginator = Paginator(products, 4)
    page_naumber = request.GET.get('page')
    products = paginator.get_page(page_naumber)
    context = {'products': products}
    return render(request, 'ecom/index.html', context=context)

