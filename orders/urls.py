from django.urls import path
from . import views

urlpatterns = [

    # MY ORDERS PAGE
    path('my-orders/', views.my_orders, name='my_orders'),

    # CANCEL ORDER
    path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),

    # DOWNLOAD INVOICE
    path('invoice/<int:order_id>/', views.download_invoice, name='invoice'),

    # ADMIN DASHBOARD
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

]