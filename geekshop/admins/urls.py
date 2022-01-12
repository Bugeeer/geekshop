from django.urls import path

from admins.views import index, UserCreateView, UserUpdateView, UserDeleteView, UserListView, CategoryListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'admins'
urlpatterns = [

    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories-create/', CategoryCreateView.as_view(), name='categories_create'),
    path('categories-update/<int:pk>', CategoryUpdateView.as_view(), name='categories_update'),
    path('categories-delete/<int:pk>', CategoryDeleteView.as_view(), name='categories_delete'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products-create/', ProductCreateView.as_view(), name='products_create'),
    path('products-update/<int:pk>', ProductUpdateView.as_view(), name='products_update'),
    path('products-delete/<int:pk>', ProductDeleteView.as_view(), name='products_delete'),

]
