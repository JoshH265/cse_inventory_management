from django.shortcuts import render
from django.http import HttpResponse
from equipment_management.models import Equipment
from . import views



# Create your views here.
def homepage(request):
    equipments = Equipment.objects.all()
    return render(request, 'home/homepage.html', {'equipments': equipments})

