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

def print_reservation(request):
    user = request.user
    userid = request.user.id
    reservation = ReservationList.objects.filter(user_id=userid).values()
    return render(request, 'user_account/userprofile.html', {'res': reservation})

def update_reservation(request):
    
    if request.method == 'POST':
        # Update the reservation with data from the POST request
        form = ReservationList(request.POST)
        form.startdate = request.POST.get('checkoutDate')
        form.enddate = request.POST.get('expectedReturnDate')
        form.quantity = request.POST.get('quantity')
        if form.is_valid():
            form.save()  # Save the updated reservation
        else:
            print(form.errors)
    
    return render(request, 'user_account/userprofile.html', {'form': form})

def delete_reservation(request):
    equipDelete = ReservationList.objects.get(equipment_id=equipment_id)
    if request.method == 'POST':
        # Delete the reservation
        equipDelete.delete()
    
    return render(request, 'user_account/userprofile.html', {'equipDelete': equipDelete})

def rebook_reservation(request):
    # Get the reservation object by its ID
    reservation = get_object_or_404(ReservationList, user_id=request.user.id)
    
    if request.method == 'POST':
        # Update the reservation with data from the POST request
        reservation.startingDate = request.POST.get('checkoutDate')
        reservation.endDate = request.POST.get('expectedReturnDate')
        reservation.quantity = request.POST.get('quantity')
        reservation.save()  # Save the updated reservation
    
    return render(request, 'user_account/userprofile.html', {'reservation': reservation})