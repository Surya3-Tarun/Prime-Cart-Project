from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Avg

from .models import Product, Category, Review


# ==============================
# HOME PAGE + SEARCH
# ==============================

def home(request):

    query = request.GET.get('q')

    categories = Category.objects.all()
    products = []

    if query:
        products = Product.objects.filter(name__icontains=query)

    return render(request, 'home.html', {
        'categories': categories,
        'products': products,
        'query': query
    })


# ==============================
# CATEGORY PRODUCTS + FILTER + SORT
# ==============================

def category_products(request, category_id):

    products = Product.objects.filter(category_id=category_id)

    # PRICE FILTER
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    # SORTING
    sort = request.GET.get('sort')

    if sort == "low":
        products = products.order_by('price')

    elif sort == "high":
        products = products.order_by('-price')

    elif sort == "new":
        products = products.order_by('-id')

    return render(request, 'category_products.html', {
        'products': products
    })


# ==============================
# PRODUCT DETAIL PAGE
# ==============================

def product_detail(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    # RELATED PRODUCTS
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]

    # REVIEWS
    reviews = Review.objects.filter(product=product)

    # AVERAGE RATING
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'related_products': related_products,
        'avg_rating': avg_rating
    })


# ==============================
# ADD REVIEW
# ==============================

def add_review(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":

        name = request.POST.get('name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            product=product,
            name=name,
            rating=rating,
            comment=comment
        )

    return redirect(f"/product/{product_id}/")


# ==============================
# LIVE SEARCH (Amazon style)
# ==============================

def live_search(request):

    query = request.GET.get('q')

    products = []

    if query:

        results = Product.objects.filter(name__icontains=query)[:5]

        for product in results:

            products.append({
                'id': product.id,
                'name': product.name
            })

    return JsonResponse(products, safe=False)