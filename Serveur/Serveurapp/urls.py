from django.urls import path

from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.base_view),


    path('Serveurapp/serveur/create/', serveur_create, name='serveur_create'),
    path('Serveurapp/serveur/update/<int:pk>/', serveur_update, name='serveur_update'),
    path('Serveurapp/serveur/detail/<int:pk>/', views.serveur_detail, name='serveur_detail'),
    path('Serveurapp/serveur/delete/<int:pk>/', serveur_delete, name='serveur_delete'),

    path('Serveurapp/application/create/', application_create, name='application_create'),
    path('Serveurapp/application/update/<int:pk>/', application_update, name='application_update'),
    path('Serveurapp/application/detail/<int:pk>/', views.application_detail, name='application_detail'),
    path('Serveurapp/application/delete/<int:pk>/', application_delete, name='application_delete'),

    path('Serveurapp/service/create/', service_create, name='service_create'),
    path('Serveurapp/service/update/<int:pk>/', service_update, name='service_update'),
    path('Serveurapp/service/detail/<int:pk>/', views.service_detail, name='service_detail'),
    path('Serveurapp/service/delete/<int:pk>/', service_delete, name='service_delete'),

    path('Serveurapp/typeserveur/create/', views.typeserveur_create, name='typeserveur_create'),
    path('Serveurapp/utilisateur/create/', views.utilisateur_create, name='utilisateur_create'),

    path('Serveurapp/generate-service-report/', generate_service_report, name='generate_service_report'),
    path('Serveurapp/upload-application/', upload_application, name='upload_application'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

