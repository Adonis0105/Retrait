# core/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

class HomeView(View):
    def get(self, request):
        return render(request, 'core/home.html')

class OperatorSelectionView(View):
    def get(self, request):
        return render(request, 'core/operator_selection.html')