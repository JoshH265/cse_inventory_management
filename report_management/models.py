from django.db import models
from authentication_app.models import User
from equipment_management.models import Equipment

class Report(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    creationDate = models.DateField()
    comments = models.TextField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
