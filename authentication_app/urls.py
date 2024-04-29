from django.urls import path
from . import views
from home.views import homepage
from equipment_management.views import equipPage
from user_account.views import user_account


urlpatterns = [
    
    path('', homepage, name=""),
    path('sign-up', views.sign_up, name="sign-up"),
    path('login', views.login, name="login"),
    path('logout', views.user_logout, name="logout"),
    path ('inventorymanagement', equipPage, name='inventorymanagement'),
    path('userprofile', user_account, name="userprofile"),
]


