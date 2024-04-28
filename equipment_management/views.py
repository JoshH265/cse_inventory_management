from django.shortcuts import render, redirect
from .models import Equipment
from .forms import EquipmentItem

def equipPage(request):
    equipments = Equipment.objects.all()  # Fetch all equipment items from the database
    context = {'equipments': equipments}
    return render(request, 'equipment_management/inventorymanagement.html', context)

def createEquipment(request):
    if request.method == "POST":
        form = EquipmentItem(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect("inventorymanagement")
        else:
            form = EquipmentItem()
    return render(request, 'equipment_management/inventorymanagement.html', {"form": form})

def Update_Equipment(request, equipment_id):
    equipment = Equipment.objects.get(pk=equipment_id)
    if request.method == "POST":
        form = EquipmentItem(request.POST, instance=equipment)
        if form.is_valid():
            form = form.save()
            return redirect("inventorymanagement")
        else:
            form = EquipmentItem(instance=equipment)
            return render(request, )

