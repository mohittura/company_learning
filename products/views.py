from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# url mapping 
# /products -> index
# uniform resource locator (address)
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products' : products})

def new(request):
    return HttpResponse("new products")