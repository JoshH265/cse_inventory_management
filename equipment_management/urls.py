from django.urls import path
from . import views
from .views import createEquipment 

urlpatterns = [
    # .as_view() because it of the class based view
    path ('inventorymanagement', views.EquipmentListView.as_view(), name='inventorymanagement'),
    path('create/', views.createEquipment, name='create_equipment'),
    # path('update/', views.updateEquipment, name='update_equipment'),
    path('update/<int:id>/', views.updateEquipment, name='update_equipment'),
]

