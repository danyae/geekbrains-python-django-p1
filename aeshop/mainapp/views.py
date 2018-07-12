from django.shortcuts import render, get_object_or_404
from .models import Product, Producer
# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'mainapp/index.html', {'products': products})


def product(request, pk):
    product_obj = get_object_or_404(Product, pk=pk)
    return render(request, 'mainapp/product.html', {'product': product_obj})
