from django.shortcuts import render
from .models import Equipment

def equipPage(request):
    equipments = Equipment.objects.all()  # Fetch all equipment items from the database
    return render(request, 'equipment_management/inventorymanagement.html', {'equipments': equipments})
