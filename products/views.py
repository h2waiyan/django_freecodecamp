from django.shortcuts import render
from .models import Product

# Create your views here.
def prodcut_detail_view(request):
    obj = Product.objects.get(id=1)
    return render(request, "products/detail.html", {})