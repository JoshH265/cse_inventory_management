from django.urls import path
from . import views
from .views import createEquipment

urlpatterns = [
    path ('inventorymanagement', views.equipPage, name='inventorymanagement'),
    path('create/', views.createEquipment, name='create_equipment'),
    path('update/', views.updateEquipment, name='update_equipment')
]

