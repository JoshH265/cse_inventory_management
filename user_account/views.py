from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reservation_management.models import Reservation
from user_account.models import UserProfile

def user_account(request):
    return render(request, 'user_account/userprofile.html')

# @login_required
# def profile(request):
#     user = request.user  # Retrieve the logged-in user
#     return render(request, 'userprofile.html', {'user': user})

# def reservation_table(request):
#     reservations = Reservation.objects.filter(user = request.user)
#     return render(request, 'userprofile.html', {'reservations': reservations})

def reservation_table(request):
    # Retrieve the user profile associated with the logged-in user
    user_profile = UserProfile.objects.get(user=request.user)
    
    # Get current reservations for the user
    current_reservations = user_profile.current_reservations()

    # Optionally, you can also get reservation history
    reservation_history = user_profile.reservation_history()

    num_reservations = current_reservations.count()

    return render(request, 'userprofile.html', {'current_reservations': current_reservations, 'reservation_history': reservation_history})