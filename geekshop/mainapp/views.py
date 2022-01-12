from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'store_name': 'GeekShop Store',
        'some_text': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! '
                     'Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=None, page=1):

    context = {
        'title': 'Geekshop | Catalog'
    }
    if id_category:
        products = Product.objects.filter(category_id=id_category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'
