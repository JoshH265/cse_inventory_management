from django.shortcuts import render
from django.http import HttpResponse
from equipment_management.models import Equipment

from .models import Equipment

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'homepage.html', {'equipments': equipments})



# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

