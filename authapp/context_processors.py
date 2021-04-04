from basket.models import Basket

# def user_status(request):
#     user = request.user
#     if user.is_authenticated:
#         status = 'Пользователь авторизован'
#     else:
#         status = 'Пользователь не авторизован'
#     return {'status': status}

def basket_count(request):
    user = request.user
    if user.is_authenticated:
        counter = Basket.objects.filter(user=user).count()
    else:
        counter = 0
    return {'basket_count': counter}
