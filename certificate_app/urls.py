# certificate_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
    path('certificate_generated/<str:certificate_id>/', views.certificate_generated, name='certificate_generated'),
    path('verify_certificate/', views.verify_certificate, name='verify_certificate'),
    path('certificate_details/<str:certificate_id>/', views.certificate_details, name='certificate_details'), 
    # Add other URL patterns here if needed
]