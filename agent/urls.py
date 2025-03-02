# agent/urls.py
from django.urls import path
from .views import OperatorSelectionView, MixxAgentFormView, MoovAgentFormView

app_name = 'agent'

urlpatterns = [
    path('select-operator/', OperatorSelectionView.as_view(), name='select_operator'),
    path('mixx-form/', MixxAgentFormView.as_view(), name='mixx_form'),
    path('moov-form/', MoovAgentFormView.as_view(), name='moov_form'),
]