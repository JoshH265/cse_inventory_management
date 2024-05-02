# from django.db import models
# from . models import Equipment

# # Create your models here.
# class equipmentHistory(models.Model):
# # to track how many times X equipment has been used
#     equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
#     date = models.DateField()
#     times_used = models.IntegerField()
    
#     def __str__(self):
#         return self.equipment.name + ' used ' + self.times_used + ' times on ' + self.date