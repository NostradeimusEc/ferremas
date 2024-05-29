from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from marketplace.models import Product


class HomeView(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(active=True)

        digital_products_data = None

        if products:
            paginator = Paginator(products, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
        
        context={
            'products':digital_products_data
        }
        return render(request, 'pages/index.html', context)
    
class ProductDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug)
        context={
            'product':product
        }
        return render(request, 'pages/products/detail.html', context)