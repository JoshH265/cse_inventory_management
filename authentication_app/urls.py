from django.urls import path
from . import views
from home.views import homepage


urlpatterns = [
    
    path('', homepage, name=""),
    path('sign-up', views.sign_up, name="sign-up"),
    path('login', views.login, name="login"),
    path('logout', views.user_logout, name="logout"),
]


