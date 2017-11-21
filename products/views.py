from django.shortcuts import render
from .models import Products

# Create your views here.
def get_index(request):
    return render(request, "base.html")
    
def all_products(request):
    products = Products.objects.all()
    return render(request, "products.html", {"products": products})