from django.shortcuts import render, redirect
from products.models import Product
from orders.models import Order, OrderItem
from coupons.models import Coupon


# CART COUNT
def cart_count(request):

    cart = request.session.get('cart', {})

    count = 0

    for item in cart.values():
        count += item['quantity']

    return {'cart_count': count}


# ADD TO CART
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id]['quantity'] += 1

    else:
        cart[product_id] = {
            'name': product.name,
            'price': float(product.price),
            'image': product.image.url,
            'quantity': 1
        }

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/cart/')


# CART PAGE
def cart_view(request):

    cart = request.session.get('cart', {})

    cart_items = []
    total_price = 0

    for product_id, item in cart.items():

        item_total = item['price'] * item['quantity']

        cart_items.append({
            'id': product_id,
            'name': item['name'],
            'price': item['price'],
            'image': item['image'],
            'quantity': item['quantity'],
            'total': item_total
        })

        total_price += item_total

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }

    return render(request, 'cart.html', context)


# INCREASE QUANTITY
def increase_quantity(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id]['quantity'] += 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/cart/')


# DECREASE QUANTITY
def decrease_quantity(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        cart[product_id]['quantity'] -= 1

        if cart[product_id]['quantity'] <= 0:
            del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/cart/')


# REMOVE PRODUCT
def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/cart/')


# CHECKOUT PAGE
def checkout_view(request):

    cart = request.session.get('cart', {})

    if not cart:
        return redirect('/cart/')

    total_price = 0

    for item in cart.values():
        total_price += item['price'] * item['quantity']

    discount = 0

    if request.method == "POST":

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')

        coupon_code = request.POST.get('coupon')

        payment_method = request.POST.get('payment')

        upi_id = request.POST.get('upi_id')
        card_number = request.POST.get('card_number')
        card_name = request.POST.get('card_name')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')


        # APPLY COUPON
        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code, active=True)
                discount = (total_price * coupon.discount) / 100
                total_price = total_price - discount
            except:
                pass


        # CREATE ORDER
        order = Order.objects.create(

            name=name,
            phone=phone,
            address=address,
            landmark=landmark,
            city=city,
            pincode=pincode,
            total_price=total_price

        )


        # CREATE ORDER ITEMS
        for product_id, item in cart.items():

            product = Product.objects.get(id=product_id)

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                price=item['price']
            )


        # CLEAR CART
        request.session['cart'] = {}

        return redirect('/order-success/')


    context = {
        'total_price': total_price,
        'discount': discount
    }

    return render(request, 'checkout.html', context)


# ORDER SUCCESS PAGE
def order_success(request):

    return render(request, 'order_success.html')