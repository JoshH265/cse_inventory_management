from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import ReservationList

def user_account(request):
    reservation = ReservationList.objects.all()
    return render(request, 'user_account/userprofile.html')

@login_required
def profile(request):
    user = request.user  # Retrieve the logged-in user
    return render(request, 'user_account/userprofile.html', {'user': user})

@login_required
def update_reservation(request, reservation_id):
    # Get the reservation object by its ID
    reservation = get_object_or_404(ReservationList, id=reservation_id, user_id=request.user.id)
    
    if request.method == 'POST':
        # Update the reservation with data from the POST request
        reservation.startingDate = request.POST.get('checkoutDate')
        reservation.endDate = request.POST.get('expectedReturnDate')
        reservation.quantity = request.POST.get('quantity')
        reservation.save()  # Save the updated reservation
    
    return render(request, 'user_account/userprofile.html', {'reservation': reservation})

@login_required
def delete_reservation(request, reservation_id):
    # Get the reservation object by its ID
    reservation = get_object_or_404(ReservationList, id=reservation_id, user_id=request.user.id)
    
    if request.method == 'POST':
        # Delete the reservation
        reservation.delete()
    
    return render(request, 'delete_reservation.html', {'reservation': reservation})

@login_required
def rebook_reservation(request, reservation_id):
    # Get the reservation object by its ID
    reservation = get_object_or_404(ReservationList, id=reservation_id, user_id=request.user.id)
    
    if request.method == 'POST':
        # Update the reservation with data from the POST request
        reservation.startingDate = request.POST.get('checkoutDate')
        reservation.endDate = request.POST.get('expectedReturnDate')
        reservation.quantity = request.POST.get('quantity')
        reservation.save()  # Save the updated reservation
    
    return render(request, 'user_account/userprofile.html', {'reservation': reservation})