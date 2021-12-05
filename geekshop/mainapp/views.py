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


def products(request):
    context = {
        'title': 'Geekshop | Catalog'
    }

    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
