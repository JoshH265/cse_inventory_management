from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment
from .forms import EquipmentItem, UpdateEquipmentItem
from .filters import EquipmentItemFilters
from django.shortcuts import redirect
from django.http import HttpResponseNotAllowed
from django.views.generic.list import ListView


def equipPage(request):
    equipment_filter = EquipmentItemFilters(request.GET, queryset=Equipment.objects.all())
    # storing the filtered form and filtered equipment queryset as context data in a variable to pass to the URL
    context = {'form': equipment_filter.form,'equipments': equipment_filter.qs}
    return render(request, 'equipment_management/inventorymanagement.html', context)


# Handling the creation of a new equipment item
def createEquipment(request):
    if request.method == "POST":
        # validating the form if the method is 'post'
        form = EquipmentItem(request.POST)
        if form.is_valid():
            # saves the new equipment item
            new_equipment = form.save()
            new_equipment.save()
            return redirect("inventorymanagement")
        else:
            # If form is not valid, print the errors to the console (for debugging purposes)
            print(form.errors)
    else:
        # if the method is 'get' an empty form is rendered to create a new item
        form = EquipmentItem()
    return render(request, 'equipment_management/inventorymanagement.html', {"form": form})

# handling updating an existing equipment item
def updateEquipment(request, id):
    # Getting the id of the equipment being accessed for updating
    equipment = Equipment.objects.get(id=id)
    if request.method == "POST":
        # if the request is 'post' the form is populated with the data in the request
        form = UpdateEquipmentItem(request.POST, instance=equipment) 
        # validating form
        if form.is_valid():
            form.save()
            return redirect("inventorymanagement")
        else:
#             # Display form errors to the user
            print(form.errors)
    else:
        form = UpdateEquipmentItem(instance=equipment)
    context = {"equipment": equipment, "form": form}
    return render(request, 'equipment_management/inventorymanagement.html', context)

# class based view for rending the database in the html page to allow for searching/filtering view
# class based to avoid multiple if statements
class EquipmentListView(ListView):
    # queryset that holds all Equipment objects
    queryset = Equipment.objects.all()
    template_name = 'equipment_management/inventorymanagement.html'
    # same as the name in the for loop on the inventory management page
    context_object_name = 'equipments'

    # overriding get_queryset method with GET paramenters
    def get_queryset(self):
        # return the queryset grabbed on line 55 by calling super
        queryset = super().get_queryset()
        self.filterset = EquipmentItemFilters(self.request.GET, queryset=queryset)
        queryset = self.filterset.qs

        sort_by = self.request.GET.get('sort-by')
        if sort_by == 'Device Name':
            queryset = queryset.order_by('equipmentName')
        elif sort_by == 'Device Type':
            queryset = queryset.order_by('equipmentType')
        elif sort_by == 'Availability':
            queryset = queryset.order_by('equipmentStatus')
        elif sort_by == 'Location':
            queryset = queryset.order_by('location')
        # returns the Equipment objects in the database matching the filters passed through the URL
        return queryset
    # overring the get_context_data method to give more context data to the inventory management page 
    def get_context_data(self, **kwargs):
        # default context data
        context = super().get_context_data(**kwargs)
        # adds the filters to equipment items as extra context data to be rendered on inventory management page
        context['form'] = self.filterset.form
        return context