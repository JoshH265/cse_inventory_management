from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment
from .forms import EquipmentItem, UpdateEquipmentItem


def equipPage(request):
    equipments = Equipment.objects.all()  # Fetch all equipment items from the database
    context = {'equipments': equipments}
    return render(request, 'equipment_management/inventorymanagement.html', context)

def createEquipment(request):
    if request.method == "POST":
        form = EquipmentItem(request.POST)
        if form.is_valid():
            new_equipment = form.save()
            # You can add any additional logic or modify fields before saving
            new_equipment.save()
            return redirect("inventorymanagement")
        else:
            # If form is not valid, print the errors to the console (for debugging purposes)
            print(form.errors)
    else:
        form = EquipmentItem()
    return render(request, 'equipment_management/inventorymanagement.html', {"form": form})


def updateEquipment(request):
    if request.method == "POST":
        id = request.POST.get('id')
        equipmentItem = Equipment.objects.get(id=id)
        form = UpdateEquipmentItem(request.POST, instance=equipmentItem) 
        if form.is_valid():
            equipmentItem.save()
        else:
            print(form.errors)
    else:
        form = EquipmentItem(instance=equipmentItem)
    context = {"equipmentItem":equipmentItem, "form": form}
    return render(request, 'equipment_management/inventorymanagement.html', context)


def DeleteEquipmentItem(request):
    equipmentItem = Equipment.objects.get(id=id)
    if request.method =="POST":
        equipmentItem.delete()
        return redirect("inventorymanagement")
    return render(request, 'equipment_management/inventorymanagement.html', {'equipmentItem': equipmentItem})
