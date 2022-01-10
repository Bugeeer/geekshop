from django.urls import path

from admins.views import index, admin_users_create, admin_users_update, admin_users_delete, admin_users, categories, \
    categories_create, categories_update, categories_delete, products, products_create, products_update, products_delete

app_name = 'admins'
urlpatterns = [

    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:pk>', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:pk>', admin_users_delete, name='admin_users_delete'),
    path('categories/', categories, name='categories'),
    path('categories-create/', categories_create, name='categories_create'),
    path('categories-update/<int:pk>', categories_update, name='categories_update'),
    path('categories-delete/<int:pk>', categories_delete, name='categories_delete'),
    path('products/', products, name='products'),
    path('products-create/', products_create, name='products_create'),
    path('products-update/<int:pk>', products_update, name='products_update'),
    path('products-delete/<int:pk>', products_delete, name='products_delete'),

]
