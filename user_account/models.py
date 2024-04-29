from django.db import models
from django.conf import settings
from reservation_management.models import Reservation

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # bio = models.TextField(blank=True)
    # # Additional fields like address, phone number, etc., can be added here.

    def current_reservations(self):
        return Reservation.objects.filter(user=self.user, isCancelled=False)

    def reservation_history(self):
        return Reservation.objects.filter(user=self.user)
