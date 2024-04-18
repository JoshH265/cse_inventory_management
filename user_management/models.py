from django.db import models
from authentication_app.models import User

class SignUpRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    # Any other fields related to the sign-up request process
