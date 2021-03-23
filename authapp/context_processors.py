def user_status(request):
    user = request.user
    if user.is_authenticated:
        status = 'Пользователь авторизован'
    else:
        status = 'Пользователь не авторизован'
    return {'status': status}