from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from mainapp.models import ProductCategory
from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCategoryForm, ProductCategoryEditForm

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_read(request):
    context = {'categories': ProductCategory.objects.all()}
    return render(request, 'adminapp/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users_read'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == 'POST':
        form = ProductCategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories_read'))
        else:
            print(form.errors)
    else:
        form = ProductCategoryForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-categories-create.html', context)

def admin_users_update(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users_read'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {'form': form, 'current_user': user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)


def admin_categories_update(request, id):
    category = ProductCategory.objects.get(id=id)
    if request.method == 'POST':
        form = ProductCategoryEditForm(data=request.POST, files=request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories_read'))
    else:
        form = UserAdminProfileForm(instance=category)
    context = {'form': form, 'current_category': category}
    return render(request, 'adminapp/admin-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    # user.delete()
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_delete(request, id):
    category = ProductCategory.objects.get(id=id)
    # category.delete()
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('admins:admin_categories_read'))