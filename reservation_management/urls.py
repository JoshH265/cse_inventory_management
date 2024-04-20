from django.urls import path
from . import views

urlpatterns = [
    path("",views.adminManagement, name='adminReservation')
]

