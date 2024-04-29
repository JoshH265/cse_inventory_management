from django.db import models
from django.conf import settings
from equipment_management.models import Equipment

class Reservation(models.Model):
    bookingDate = models.DateTimeField()
    checkoutDate = models.DateTimeField()
    expectedReturnDate = models.DateTimeField()
    approvalStatus = models.CharField(max_length=100) # PROBABLY CHANGE THE VALUE TO BOOLEAN
    isCancelled = models.BooleanField(default=False)
    quantity = models.IntegerField(default=False)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
