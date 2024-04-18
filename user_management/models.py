from django.conf import settings
from django.db import models

class SignUpRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    # Any other fields related to the sign-up request process
