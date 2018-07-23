from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    return render(request, 'mainapp/index.html',
                  {'products_dict': products_dict})


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'mainapp/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        # Products of the same producer
        context['other_products'] = Product.objects.filter(
            producer=self.object.producer).exclude(pk=self.object.pk)
        return context


def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'mainapp/product/add.html', {'form': form})


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'price', 'text', 'producer', 'image']
    template_name = 'mainapp/product/create.html'

    def get_success_url(self):
        success_url = reverse_lazy('product_detail', args=(self.object.pk,))
        return success_url


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'price', 'text', 'producer', 'image']
    template_name = 'mainapp/product/create.html'

    def get_success_url(self):
        success_url = reverse_lazy('product_detail', args=(self.object.pk,))
        return success_url


class ProductDelete(DeleteView):
    model = Product
    template_name = 'mainapp/product/confirm_delete.html'
    success_url = reverse_lazy('index')
