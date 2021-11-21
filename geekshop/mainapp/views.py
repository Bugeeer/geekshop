from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'Geekshop Catalog', }
    return render(request, 'mainapp/products.html', context)