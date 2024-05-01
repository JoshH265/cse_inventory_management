from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import redirect
from .useraccount_models import ReservationList

from reservation_management.models import Reservation
from equipment_management.models import Equipment

def user_account(request):
    reservation = Reservation.objects.all()
    print(len(reservation))
    return render(request, 'user_account/userprofile.html', {'reservation': reservation})

@login_required
def profile(request):
    user = request.user  # Retrieve the logged-in user
    return render(request, 'user_account/userprofile.html', {'user': user})

def print_reservation(request):
    user = request.user
    userid = user.id
    res = Reservation.objects.filter(user_id=userid).values()
    print(res)
    return render(request, 'user_account/userprofile.html', {'res': res})

def update_reservation(request):
    
    if request.method == 'POST':
        # Update the reservation with data from the POST request
        form = ReservationList(request.POST)
        form.startdate = request.POST.get('checkoutDate')
        form.enddate = request.POST.get('expectedReturnDate')
        form.quantity = request.POST.get('quantity')
        if form.is_valid():
            form.save()  # Save the updated reservation
            return redirect("userprofile")
        else:
            print(form.errors)
    
    return render(request, 'user_account/userprofile.html', {'form': form})

def delete_reservation(request, equipment_id):
    # Retrieve the reservation to delete using the equipment_id
    equipDelete = get_object_or_404(ReservationList, equipment_id=equipment_id)
    
    if request.method == 'POST':
        # Delete the reservation
        equipDelete.delete()
        print("Reservation deleted successfully")  # Debugging
        return redirect("userprofile")
    else:
        print("Request method is not POST")  # Debugging
    # Return the response (redirect or render)
    return render(request, 'user_account/userprofile.html', {'equipDelete': equipDelete})

def rebook_reservation(request):
    # Get the reservation object by its ID
    rebook = get_object_or_404(ReservationList, user_id=request.user.id)
    
    if request.method == 'POST':
        # Update the reservation with data from the POST request
        rebook.startingDate = request.POST.get('checkoutDate')
        rebook.endDate = request.POST.get('expectedReturnDate')
        rebook.quantity = request.POST.get('quantity')
        rebook.save()  # Save the updated reservation
    
    return render(request, 'user_account/userprofile.html', {'rebook': rebook})