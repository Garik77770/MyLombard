from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    # """Домашняя страница"""
    path('*', views.basket_detail, name='basket_detail'),
    # """Страница по категориям"""
    path('add/<int:product_id>/', views.basket_add, name='basket_add'),
    # """Страница продукта"""
    path('remove/<int:product_id>/', views.basket_remove, name='basket_remove'),
]
