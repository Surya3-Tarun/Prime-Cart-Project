from django.shortcuts import render, redirect
from .models import Wishlist
from products.models import Product


# Wishlist Page
def wishlist_view(request):

    wishlist_items = Wishlist.objects.all()

    context = {
        'wishlist_items': wishlist_items
    }

    return render(request, 'wishlist.html', context)


# Add product to wishlist
def add_to_wishlist(request, product_id):

    product = Product.objects.get(id=product_id)

    # avoid duplicates
    Wishlist.objects.get_or_create(product=product)

    return redirect('/')


# Remove product from wishlist
def remove_from_wishlist(request, product_id):

    Wishlist.objects.filter(product_id=product_id).delete()

    return redirect('/wishlist/')


# Wishlist count for navbar
def wishlist_count(request):

    count = Wishlist.objects.count()

    return {'wishlist_count': count}