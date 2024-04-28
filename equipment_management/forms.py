from django import forms
from .models import Equipment 

class EquipmentItem (forms.ModelForm):

    class Meta:
        model = Equipment
        fields = "__all__"