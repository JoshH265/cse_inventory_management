from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
