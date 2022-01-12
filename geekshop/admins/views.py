from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryUpdateFormAdmin, ProductUpdateFormAdmin
from authapp.models import User
from mainapp.mixin import CustomDispatchMixin, BaseClassContextMixin, UserDispatchMixin
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


# Users
class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    ttitle = 'Админ | Пользователи'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админ | Создание пользователя'


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin-categories')
    title = 'Админ | Изменение пользователя'


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админ | Удаление пользователя'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Category
class CategoryListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    title = 'Админ | Категории'


class CategoryCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    form_class = CategoryUpdateFormAdmin
    success_url = reverse_lazy('admins:categories')
    title = 'Админ | Создание категории'


class CategoryUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryUpdateFormAdmin
    success_url = reverse_lazy('admins:categories')
    title = 'Админ | Изменение категории'


class CategoryDeleteView(DeleteView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Product
class ProductListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-read.html'
    title = 'Админ | Продукты'


class ProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-create.html'
    form_class = ProductUpdateFormAdmin
    success_url = reverse_lazy('admins:products')
    title = 'Админ | Создание продукта'


class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-category-update-delete.html'
    form_class = ProductUpdateFormAdmin
    success_url = reverse_lazy('admins:categories')
    title = 'Админ | Изменение продукта'


# @user_passes_test(lambda u: u.is_superuser)
# def products_update(request, pk):
#     product_select = Product.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ProductUpdateFormAdmin(data=request.POST, instance=product_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:products'))
#     else:
#         form = ProductUpdateFormAdmin(instance=product_select)
#     context = {
#         'title': 'Geekshop - Админ | Обновление продукта',
#         'form': form,
#         'product_select': product_select,
#     }
#     return render(request, 'admins/admin-product-update-delete.html', context)


class ProductDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    success_url = reverse_lazy('admins:products')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
