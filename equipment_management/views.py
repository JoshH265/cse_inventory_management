from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipmentItem
from .models import Equipment

def equipPage(request):
    equipments = Equipment.objects.all()  # Fetch all equipment items from the database
    context = {'equipments': equipments}
    return render(request, 'equipment_management/inventorymanagement.html', context)

def createEquipment(request):
    if request.method == "POST":
        form = EquipmentItem(request.POST)
        if form.is_valid():
            new_equipment = form.save(commit=False)
            # You can add any additional logic or modify fields before saving
            new_equipment.save()
            return redirect("inventorymanagement")
        else:
            # If form is not valid, print the errors to the console (for debugging purposes)
            print(form.errors)
    else:
        form = EquipmentItem()
    return render(request, 'equipment_management/inventorymanagement.html', {"form": form})

# def createEquipment(request):
#     if request.method == "POST":
#         form = EquipmentItem(request.POST)
#         if form.is_valid():
#             action = request.POST.get('action')
#             if action == 'create':
#                 form.save()
#                 return redirect("inventorymanagement")
#         else:
#             form = EquipmentItem()
#     return render(request, 'equipment_management/inventorymanagement.html', {"form": form})

def Update_Equipment(request, equipment_id):
    
    if request.method == "POST":
        form = EquipmentItem(request.POST)
        if form.is_valid():
            action = request.POST.get('action')
            if action == 'update':
                equipment_id = request.POST.get('equipment_id')
                equipment = Equipment.objects.get(pk=equipment_id)
            form = form.save()
            return redirect("inventorymanagement")
        else:
            form = EquipmentItem(instance=equipment)
            return render(request, 'equipment_management/inventorymanagement.html', {"form": form})
