from django.shortcuts import render


# Create your views here.
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'store_name': 'GeekShop Store',
        'some_text': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! '
                     'Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'title': 'Geekshop Catalog'}

    context['products'] = Product.objects.all()
    context['category'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)
