from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum
from django.utils.timezone import now
from reportlab.pdfgen import canvas

from .models import Order
from products.models import Product


# ==============================
# MY ORDERS PAGE
# ==============================

def my_orders(request):

    orders = Order.objects.prefetch_related('items__product').all()

    return render(request, 'my_orders.html', {
        'orders': orders
    })


# ==============================
# CANCEL ORDER
# ==============================

def cancel_order(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    order.status = "Cancelled"
    order.save()

    return redirect('/my-orders/')


# ==============================
# DOWNLOAD INVOICE
# ==============================

def download_invoice(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order.id}.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica", 16)
    p.drawString(200, 800, "PrimeCart Invoice")

    p.setFont("Helvetica", 12)

    p.drawString(50, 760, f"Order ID: {order.id}")
    p.drawString(50, 740, f"Customer: {order.name}")
    p.drawString(50, 720, f"Phone: {order.phone}")
    p.drawString(50, 700, f"Address: {order.address}")
    p.drawString(50, 680, f"Total Price: ₹ {order.total_price}")

    y = 640

    for item in order.items.all():

        p.drawString(50, y, f"{item.product.name}")
        p.drawString(300, y, f"Qty: {item.quantity}")
        p.drawString(400, y, f"₹ {item.price}")

        y -= 20

    p.save()

    return response


# ==============================
# ADMIN DASHBOARD
# ==============================

def admin_dashboard(request):

    # TOTAL ORDERS
    total_orders = Order.objects.count()

    # TODAY ORDERS
    today_orders = Order.objects.filter(
        created_at__date=now().date()
    ).count()

    # TOTAL REVENUE
    total_revenue = Order.objects.aggregate(
        Sum('total_price')
    )['total_price__sum']

    # TOTAL PRODUCTS
    total_products = Product.objects.count()

    if total_revenue is None:
        total_revenue = 0

    context = {
        'total_orders': total_orders,
        'today_orders': today_orders,
        'total_revenue': total_revenue,
        'total_products': total_products
    }

    return render(request, 'admin_dashboard.html', context)