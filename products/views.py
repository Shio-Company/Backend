# products/views.py
from django.http import JsonResponse
from .models import Product
from django.db.models import Sum

def inventory_summary(request):
    products = Product.objects.all()
    data = []
    for product in products:
        total_stock = product.variations.aggregate(total=Sum('stock_quantity'))['total'] or 0
        data.append({
            "name": product.name,
            "total_stock": total_stock,
        })
    return JsonResponse({"inventory": data})