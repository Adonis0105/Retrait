# core/urls.py
from django.urls import path
from .views import HomeView, OperatorSelectionView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('select-operator/', OperatorSelectionView.as_view(), name='select_operator'),
]