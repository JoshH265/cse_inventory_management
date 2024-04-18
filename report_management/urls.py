from django.urls import path
from . import views

urlpatterns = [
    
    path('home', views.home, name="home"),
    path('report_management', views.report_manager, name="report_management"),
    
]