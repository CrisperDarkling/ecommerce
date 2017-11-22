from django.shortcuts import render
from .models import Products

# Create your views here.

def all_products(request):
    products = Products.objects.all()
    return render(request, "products.html", {'products': products})
    
def do_search(request):
    products = Products.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})