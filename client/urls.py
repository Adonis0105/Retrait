# client/urls.py
from django.urls import path
from .views import ScanQRView, ProcessMixxQRView, ProcessMoovQRView

app_name = 'client'

urlpatterns = [
    path('scan/', ScanQRView.as_view(), name='scan'),
    path('process-mixx/', ProcessMixxQRView.as_view(), name='process_mixx'),
    path('process-moov/', ProcessMoovQRView.as_view(), name='process_moov'),
]