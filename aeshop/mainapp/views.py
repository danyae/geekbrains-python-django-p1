from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Producer
from .forms import ProductForm
# Create your views here.


def index(request):
    producers = Producer.objects.filter(active=True)
    products_dict = {}
    for producer in producers:
        products_for_producer = Product.objects.filter(
            producer__name=producer.name)
        if len(products_for_producer) > 0:
            products_dict[producer] = products_for_producer
    return render(request, 'mainapp/index.html', {'products_dict': products_dict})


def product(request, pk):
    product_obj = get_object_or_404(Product, pk=pk)
    producs_same_producer = Product.objects.filter(
        producer=product_obj.producer).exclude(pk=product_obj.pk)
    return render(request, 'mainapp/product.html', {'product': product_obj,
                                                    'other_products': producs_same_producer})


def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'mainapp/product/add.html', {'form': form})
