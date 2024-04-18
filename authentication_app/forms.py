from django.contrib.auth.forms import UserCreationForm
from authentication_app.models import CustomUser
# from django.contrib.auth.models import User
from django import forms


class UserCreation(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    roleType = forms.CharField(max_length=50, required=False)  # Set required to True if needed
    accountStatus = forms.CharField(max_length=50, required=False)  # Set required to True if needed

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'roleType', 'accountStatus']
    
    def __init__(self, *args, **kwargs):
        super(UserCreation, self).__init__(*args, **kwargs)
        # Remove help text
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


