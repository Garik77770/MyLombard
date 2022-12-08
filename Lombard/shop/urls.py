from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # """Домашняя страница"""
    path('', views.product_list, name='product_list'),
    # """Страница по категориям"""
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # """Страница продукта"""
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('price_list', views.price_list, name='price_list'),

]