from django.shortcuts import render


# Create your views here.

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
        'title': 'Geekshop Catalog',
        'product': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.',
             'info': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб..',
             'info': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.',
             'info': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.',
             'info': 'Плотная ткань. Легкий материал.'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00 руб.',
             'info': 'Гладкий кожаный верх. Натуральный материал.'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00 руб.',
             'info': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ]
    }
    return render(request, 'mainapp/products.html', context)
