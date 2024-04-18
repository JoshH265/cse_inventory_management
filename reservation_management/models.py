from django.db import models
from authentication_app.models import User
from equipment_management.models import Equipment

class Reservation(models.Model):
    bookingDate = models.DateTimeField()
    checkoutDate = models.DateTimeField()
    expectedReturnDate = models.DateTimeField()
    approvalStatus = models.CharField(max_length=100)
    isCancelled = models.BooleanField(default=False)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
