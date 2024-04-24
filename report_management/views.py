from django.shortcuts import render
from home.views import homepage


def home(request):
    return homepage(request)

# Create your views here.
def report_manager(request):
    return render(request, 'report_management/reportmanagement.html')
