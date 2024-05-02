from django.db import models

class Equipment(models.Model):

    Status_Choices = [
        ('On_loan', 'On Loan'),
        ('Repairing', 'Repairing'),
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable')
    ]
    
    Location_choices = [
        ('blue_cabinet', 'XRLab Blue Cabinet'),
        ('blue_cabinet_large', 'XRLab Blue Cabinet Large'),
        ('medium_wooden_cabinet', 'XRLab Medium Wooden Cabinet'),
        ('other', 'Other'),
    ]

    equipmentName = models.CharField(max_length=100)
    equipmentStatus = models.CharField(max_length=100, choices=Status_Choices, default='Available')
    equipmentType = models.CharField(max_length=100)
    quantity = models.IntegerField()
    auditDate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, choices=Location_choices)
    accessLevel = models.CharField(max_length=100, null=True, blank=True)
    serialNo = models.CharField(max_length=100, null=True, blank=True)
    comments = models.TextField(max_length=250, null=True, blank=True)
    bookingCount = models.PositiveIntegerField (default=0, null=True, blank=True)