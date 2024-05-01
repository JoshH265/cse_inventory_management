from django.db import models
from django.conf import settings
from equipment_management.models import Equipment

class Reservation(models.Model):
    id = models.BigIntegerField(default=0, primary_key=True)
    bookingDate = models.DateTimeField()
    checkoutDate = models.DateTimeField()
    expectedReturnDate = models.DateTimeField()
    approvalStatus = models.CharField(max_length=100)
    isCancelled = models.BooleanField(default=False)
    quantity = models.IntegerField(default=False)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)
    activeReservation = models.BooleanField(default=True)