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
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '6 090,00',
             'info': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'image': 'vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face',
             'price': '23 725,00',
             'info': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'image': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': '3 390,00',
             'info': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage',
             'price': '2 340,00',
             'info': 'Плотная ткань. Легкий материал.',
             'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': '13 590,00',
             'info': 'Гладкий кожаный верх. Натуральный материал.',
             'image': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': '2 890,00',
             'info': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        ]
    }
    return render(request, 'mainapp/products.html', context)
