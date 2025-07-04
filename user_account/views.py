from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from reservation_management.models import Reservation
from .forms import ReservationForm
from django.http import HttpResponse
from django.template import loader

def user_account(request):
    user = request.user
    userid = user.id
    reservation = Reservation.objects.filter(user_id=userid, activeReservation=True)
    resActive = Reservation.objects.filter(user_id=userid, activeReservation=False)

    # return render(request, 'user_account/userprofile.html', {'reservation': reservation}, {'resActive': resActive})
    userprofile = loader.get_template('user_account/userprofile.html')
    context = {'reservation': reservation, 'resActive': resActive}
    return HttpResponse(userprofile.render(context, request))


# def print_inactiveReservation(request):
#     user = request.user
#     userid = user.id
#     resActive = Reservation.objects.filter(user_id=userid, activeReservation=False)
#     print(len(resActive))
#     return render(request, 'user_account/userprofile.html', {'resActive': resActive})

def profile(request):
    user = request.user  # Retrieve the logged-in user
    return render(request, 'user_account/userprofile.html', {'user': user})

def print_reservation(request):
    user = request.user
    userid = user.id
    res = Reservation.objects.filter(user_id=userid).values()
    print(res)
    return render(request, 'user_account/userprofile.html', {'res': res})
    # context = {'reservation': reservation, 'resActive': resActive}
    #userprofile = loader.get_template('user_account/userprofile.html')
    #return HttpResponse(userprofile.render({'res': res}, request))

def update_reservation(request, id):
    reservation = Reservation.objects.get(id=id)
    form = ReservationForm(instance=reservation)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    
    return render(request, 'user_account/userprofile.html', {'form': form})
    #userprofile = loader.get_template('user_account/userprofile.html')
    #return HttpResponse(userprofile.render( {'form': form}, request))

def delete_reservation(request, id):
    # Retrieve the reservation object from the database
    equipDelete = Reservation.objects.get(id=id)
    
    if request.method == 'POST':
        # If the request method is POST, delete the reservation
        equipDelete.delete()
        # Redirect to the same page or wherever appropriate
        return redirect('userprofile.html')
    
    # return render(request, 'user_account/delete_reservation.html', {'equipDelete': equipDelete})
    userprofile = loader.get_template('user_account/userprofile.html')
    return HttpResponse(userprofile.render( {'equipDelete': equipDelete}, request))

def rebook_reservation(request):
    # Get the reservation object by its ID
    rebook = get_object_or_404(Reservation, user_id=request.user.id)
    
    if request.method == 'POST':
        # Update the reservation with data from the POST request
        rebook.startingDate = request.POST.get('checkoutDate')
        rebook.endDate = request.POST.get('expectedReturnDate')
        rebook.quantity = request.POST.get('quantity')
        rebook.save()  # Save the updated reservation
    
    # return render(request, 'user_account/userprofile.html', {'rebook': rebook})
    userprofile = loader.get_template('user_account/userprofile.html')
    return HttpResponse(userprofile.render({'rebook': rebook}, request))