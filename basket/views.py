from django.shortcuts import HttpResponseRedirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.template.loader import render_to_string
# from django.http import JsonResponse

from mainapp.models import Product
from basket.models import Basket


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def basket_edit(request, id, quantity):
#     if request.is_ajax():
#         quantity = int(quantity)
#         basket = Basket.objects.get(id=int(id))
#         if quantity > 0:
#             basket.quantity = quantity
#             basket.save()
#         else:
#             basket.delete()
#         baskets = Basket.objects.filter(user=request.user)
#         context = {
#             'baskets': baskets,
#         }
#         result = render_to_string('basket/basket.html', context)
#         return JsonResponse({'result': result})