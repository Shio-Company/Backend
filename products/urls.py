from django.urls import path
from .views import inventory_summary 

urlpatterns = [
    path('inventory/', inventory_summary, name='inventory_summary'),
]