from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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

# def products(request, id=None):
#     if id:
#         context ={
#             'product': Product.objects.get(id=id)
#         }
#     else:
#         context = {
#             'products': Product.objects.all(),
#             'categories': ProductCategory.objects.all(),
#          }
#     return render(request, 'mainapp/products.html', context)

# def products(request, category_id=None):
#     context = {
#         'categories': ProductCategory.objects.all(),
#         'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
#     }
#     return render(request, 'mainapp/products.html', context)

def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
    else:
        products = Product.objects.all().order_by('price')
    per_page = 2
    paginator = Paginator(products.order_by('name'), per_page)
    # products_paginator = paginator.page(page)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {'categories': ProductCategory.objects.all(), 'products': products_paginator}
    return render(request, 'mainapp/products.html', context)