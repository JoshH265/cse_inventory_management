from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment
from .forms import EquipmentItem, UpdateEquipmentItem
from django.shortcuts import redirect
from django.http import HttpResponseNotAllowed


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

from .forms import UpdateEquipmentItem
from .models import Equipment

def updateEquipment(request, id):
    equipment = Equipment.objects.get(id=id)
    if request.method == "POST":
        form = UpdateEquipmentItem(request.POST, instance=equipment) 
        if form.is_valid():
            form.save()
            for field, value in request.POST.items():
                print(f"{field}: {value}")
            return redirect("inventorymanagement")
        else:
#             # Display form errors to the user
            print(form.errors)
            for field, value in request.POST.items():
                print(f"{field}: {value}")
                return redirect("inventorymanagement")
    else:
        form = UpdateEquipmentItem(instance=equipment)
    context = {"equipment": equipment, "form": form}
    return render(request, 'equipment_management/inventorymanagement.html', context)



# THIS DOESNT WORK, WILL WORK ON IT TOMORROW
# def deleteEquipment(request, id):
#     if request.method == 'POST':
#         equipment = Equipment.objects.get(id=id)
#         equipment.delete()
#         return redirect('inventorymanagement')
#     else:
#         return HttpResponseNotAllowed(['POST'])