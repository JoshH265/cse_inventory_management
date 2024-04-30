from django.db import models

class ReservationList(models.Model):
    
    bookingDate = models.DateField()
    checkoutDate = models.DateField()
    expectedReturnDate = models.DateField()
    approvalStatus = models.CharField(max_length=100)
    isCancelled = models.BooleanField(default=False)
    equipment_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
