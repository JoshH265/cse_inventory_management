from django import forms
from reservation_management.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['quantity', 'checkoutDate', 'expectedReturnDate', 'activeReservation']  # Specify the fields to include in the form
