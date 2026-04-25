from django.urls import path
from . import views

urlpatterns = [

    path('cart/', views.cart_view, name='cart'),

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('increase/<int:product_id>/', views.increase_quantity, name='increase'),

    path('decrease/<int:product_id>/', views.decrease_quantity, name='decrease'),

    path('checkout/', views.checkout_view, name='checkout'),

    path('order-success/', views.order_success, name='order_success')

]