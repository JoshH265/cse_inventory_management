from django.urls import path
from . import views

urlpatterns = [
    path('reportmanagement', views.report_manager, name="reportmanagement"),
    
]