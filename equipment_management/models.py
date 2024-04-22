from django.db import models

class Equipment(models.Model):
    equipmentName = models.CharField(max_length=100)
    equipmentCondition = models.CharField(max_length=100)
    equipmentType = models.CharField(max_length=100)
    quantity = models.IntegerField()
    auditDate = models.DateField()
    location = models.CharField(max_length=100)
    siteLocation = models.CharField(max_length=100)
    accessLevel = models.CharField(max_length=100)
    serialNo = models.CharField(max_length=100)
    CPU = models.CharField(max_length=100)
    RAM = models.IntegerField()
    GPU = models.CharField(max_length=100)
    comments = models.TextField()
