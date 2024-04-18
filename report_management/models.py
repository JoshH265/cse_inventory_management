from django.db import models
from django.conf import settings
from equipment_management.models import Equipment

class Report(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    creationDate = models.DateField()
    comments = models.TextField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
