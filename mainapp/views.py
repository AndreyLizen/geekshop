from django.shortcuts import render
from mainapp.models import Product, ProductCategory
# Create your views here.


def main(request):
    # context = {
    #     'title': "тестовый заголовок",
    #     'products': [
    #         {'name': 'Товар1', 'price': "1000руб."},
    #         {'name': 'Товар2', 'price': "2000руб."},
    #         {'name': 'Товар3', 'price': "3000руб."},
    #     ]
    # }
    # return render(request, 'mainapp/index.html', context)

    return render(request, 'mainapp/index.html')

def products(request):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)