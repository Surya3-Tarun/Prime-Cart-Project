from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),

    # PRODUCTS
    path('', include('products.urls')),

    # CART
    path('', include('cart.urls')),

    # WISHLIST
    path('', include('wishlist.urls')),

    # ORDERS
    path('', include('orders.urls')),

    # USERS AUTHENTICATION
    path('', include('users.urls')),

    # GOOGLE LOGIN (django-allauth)
    path('accounts/', include('allauth.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)