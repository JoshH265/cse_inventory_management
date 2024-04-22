from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name=""),
    path('sign-up', views.sign_up, name="sign-up"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout, name="logout"),
]


