from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authentication_app.models import CustomUser
from django import forms

from django.forms.widgets import PasswordInput, TextInput



# User registration form Model
class UserCreation(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    roleType = forms.CharField(widget=forms.HiddenInput(), max_length=50, required=False)  
    accountStatus = forms.CharField(widget=forms.HiddenInput(), max_length=50, required=False)

    password2 = forms.CharField(
        label= ("Confirm Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'roleType', 'accountStatus']
    
    def __init__(self, *args, **kwargs):
        super(UserCreation, self).__init__(*args, **kwargs)
        # Remove help text
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

# User sign in form Model

class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))

