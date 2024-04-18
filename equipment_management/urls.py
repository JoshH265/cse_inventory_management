from django.urls import path
from .import views

urlpatterns = [
    path ('inventorymanagement', views.equipPage, name='inventorymanagement')
]

