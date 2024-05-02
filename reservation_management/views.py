from django.shortcuts import render
from .models import Reservation
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def adminManagement(request):  
    # get the objects from the reservations db
    reservations = Reservation.objects.select_related('equipment', 'user').all()
    # filter out the approved equipments 
    approved_reservations = Reservation.objects.select_related('equipment', 'user').filter(approvalStatus = 'True')

    # Search query and sort query
    search_query = request.GET.get('q', '')
    sort_by = request.GET.get('sort_by', '')
    # if statement for the search query that run if any condiiton is met
    if search_query:
        reservations = reservations.filter(
            Q(user__username__icontains=search_query) |
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query) |
            Q(equipment__equipmentName__icontains=search_query) |
            Q(equipment__equipmentType__icontains=search_query)
        )
        approved_reservations = approved_reservations.filter(
            Q(user__username__icontains=search_query) |
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query) |
            Q(equipment__equipmentName__icontains=search_query) |
            Q(equipment__equipmentType__icontains=search_query)
        )

    # setting the sort by the date booked based on the html option
    if sort_by == 'new':
        reservations = reservations.order_by('-bookingDate')
        approved_reservations = approved_reservations.order_by('-bookingDate')
    elif sort_by == 'old':
        reservations = reservations.order_by('bookingDate')
        approved_reservations = approved_reservations.order_by('bookingDate')
        # data dictionary
    dataInfo = {
        'reservations': reservations,
        'approved_reservations': approved_reservations
    }

    return render(request, 'reservation_management/adminReservation.html', dataInfo)
# log in required basically
@login_required
def profile(request):
    user = request.user  # Retrieve the logged-in user
    return render(request, 'reservation_management/adminReservation.html', {'user': user})