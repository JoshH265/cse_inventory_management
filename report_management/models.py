from django.db import models
from django.conf import settings
from equipment_management.models import Equipment
from reservation_management.models import Reservation
import datetime
from django.utils.timezone import now

# class Report(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     creationDate = models.DateField()
#     comments = models.TextField()
#     equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)ls

class Report(models.Model):
    name = models.CharField(max_length=200, default='Default Report Name')
    report_type = models.CharField(max_length=100, verbose_name="Report Type", null=True)
    date_created = models.DateField(default=now)  # 'now' without parentheses
    pdf = models.FileField(upload_to='reports/', verbose_name="PDF File")

    def __str__(self):
        return f"{self.name} ({self.date_created})"
