from django.shortcuts import render

def equipPage (request):
    return render (request, 'equipment_management/inventorymanagement.html')