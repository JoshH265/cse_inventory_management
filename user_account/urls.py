from django.urls import path
from . import useraccount_views

urlpatterns = [
    path('userprofile/', useraccount_views.user_account, name="userprofile"),   
    path('update_reservation/', useraccount_views.update_reservation, name='update_reservation'),
    path('update_reservation/<int:res>', useraccount_views.update_reservation, name='update_reservation'),
    path('delete_reservation/', useraccount_views.delete_reservation, name='delete_reservation'),
    path('delete_reservation/<int:equipment_id>', useraccount_views.delete_reservation, name='delete_reservation'),
]
