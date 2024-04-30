from django.shortcuts import render
from .models import Reservation
from django.contrib.auth.decorators import login_required

# Create your views here.
def adminManagement(request):  
    reservations = Reservation.objects.select_related('equipment', 'user').all()
    dataInfo = {'reservations' : reservations}
    return render(request, 'reservation_management/adminReservation.html', dataInfo)

@login_required
def profile(request):
    user = request.user  # Retrieve the logged-in user
    return render(request, 'reservation_management/adminReservation.html', {'user': user})
