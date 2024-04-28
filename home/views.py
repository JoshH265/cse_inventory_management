from django.shortcuts import render
from django.http import HttpResponse
from equipment_management.models import Equipment


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

