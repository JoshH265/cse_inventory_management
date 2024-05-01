from django.db import models
from django.conf import settings
from equipment_management.models import Equipment

class ReservationList(models.Model):
    
    bookingDate = models.DateField()
    checkoutDate = models.DateField()
    expectedReturnDate = models.DateField()
    approvalStatus = models.CharField(max_length=100)
    isCancelled = models.BooleanField(default=False)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)