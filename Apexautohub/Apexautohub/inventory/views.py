from django.shortcuts import render

def inventory_view(request):
    return render(request, 'Inventory/inventory.html')

def brand1_view(request):
    return render(request, 'Inventory/TATA/brand1.html')

def tata1_view(request):
    return render(request, 'Inventory/TATA/tata1.html')

def tata2_view(request):
    return render(request, 'Inventory/TATA/tata2.html')

