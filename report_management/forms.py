# forms.py
from django import forms

class ReportForm(forms.Form):
    REPORT_CHOICES = [
        ('inventory_status', 'Inventory Status'),
        ('equipment_usage', 'Equipment Usage History'),
        ('audit_status', 'Audit Status'),
        ('overdue_equipment', 'Overdue Equipment'),
        # Add other report types as needed
    ]
    
    report_type = forms.ChoiceField(choices=REPORT_CHOICES)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
