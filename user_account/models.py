from django.db import models
from django.conf import settings
from equipment_management.models import Equipment

class ReservationList(models.Model):
    
    id = models.BigIntegerField(default=0, primary_key=True)
    bookingDate = models.DateField(blank=True, null=True)
    checkoutDate = models.DateField()
    expectedReturnDate = models.DateField()
    approvalStatus = models.CharField(max_length=100)
    isCancelled = models.BooleanField(default=False)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)