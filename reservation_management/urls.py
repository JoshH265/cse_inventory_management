from django.urls import path
from . import views

urlpatterns = [
    path("adminReservation",views.adminManagement, name='adminReservation')
]

