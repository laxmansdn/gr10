from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from category.models import Category
from .models import Product

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    if product_count == 1:
        item1 = f'{product_count} Item found'
        product_count = item1
    elif product_count == 0:
        item2 = f'No Item found'
        product_count = item2
    else:
        item3 = f'{product_count} Items found'
        product_count = item3

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)
