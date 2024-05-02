from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from authentication_app.views import user_logout


urlpatterns = [
    path('reportmanagement', views.report_manager, name="reportmanagement"),
    path('generate-report', views.generate_report, name='generate_report'),
    path('logout/', user_logout, name='logout'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
