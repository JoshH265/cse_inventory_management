from django.urls import path
from . import useraccount_views

urlpatterns = [
    path('userprofile', useraccount_views.user_account, name="userprofile"),   
]

