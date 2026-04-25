from django.shortcuts import render
from products.models import Product

from django.http import HttpResponse
from django.core.management import call_command


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def load_data(request):
    try:
        call_command('loaddata', 'data.json')
        return HttpResponse("Data loaded successfully ✅")
    except Exception as e:
        return HttpResponse(f"Error: {e}")