from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    roleType = models.CharField(max_length=50)
    accountStatus = models.CharField(max_length=50)
