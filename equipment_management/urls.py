from django.urls import path
from . import views
from .views import createEquipment

urlpatterns = [
    path ('inventorymanagement', views.equipPage, name='inventorymanagement'),
    path('create/', views.createEquipment, name='create_equipment'),
    # path('equipment/<int:equipment_id>/edit/', createEquipment, name='update_equipment'),  # For updating existing equipment
]

