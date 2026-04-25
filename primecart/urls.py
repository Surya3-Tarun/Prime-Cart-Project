from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# Load data view
from primecart.views import load_data


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Load Data (only for testing - later remove chey)
    path('load-data/', load_data, name='load_data'),

    # Apps URLs
    path('', include('products.urls')),
    path('', include('cart.urls')),
    path('', include('wishlist.urls')),
    path('', include('orders.urls')),
    path('', include('users.urls')),

    # Authentication (Google login - allauth)
    path('accounts/', include('allauth.urls')),

]


# MEDIA files serve (ONLY for development / DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)