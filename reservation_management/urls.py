from django.urls import path
from . import views

urlpatterns = [
    path("reservation_management",views.adminManagement, name='adminReservation')
]

