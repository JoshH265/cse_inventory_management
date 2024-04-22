from django.shortcuts import render

# Create your views here.
def adminManagement(request):
    return render(request, 'reservation_management/adminReservation.html')