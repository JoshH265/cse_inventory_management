import django_filters
from .models import Equipment

class EquipmentItemFilters(django_filters.FilterSet):
    # allows the user to specify a range for the quantity
    quantity = django_filters.RangeFilter()

    # exact allows the user to pick from a drop down
    class Meta:
        model = Equipment
        fields = {
            'equipmentName': ['icontains'] , 
            'equipmentType': ['icontains'], 
            'equipmentStatus': ['exact'],
            'location': ['exact']
        }