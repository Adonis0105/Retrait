# agent/views.py
import qrcode # type: ignore
import json
import os
import base64
from io import BytesIO
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.urls import reverse
from .forms import MixxAgentForm, MoovAgentForm
from core.models import QRCode

class OperatorSelectionView(View):
    def get(self, request):
        return render(request, 'agent/operator_selection.html')

class MixxAgentFormView(View):
    def get(self, request):
        form = MixxAgentForm()
        return render(request, 'agent/mixx_form.html', {'form': form})
    
    def post(self, request):
        form = MixxAgentForm(request.POST)
        if form.is_valid():
            agent_number = form.cleaned_data['agent_number']
            
            # Création des données à encoder dans le QR
            data = {
                'operator': 'mixx',
                'agent_number': agent_number
            }
            
            # Création du QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            
            # Création d'une URL avec les paramètres
            base_url = request.build_absolute_uri(reverse('client:process_mixx'))
            url_params = f"?agent_number={agent_number}"
            qr_data = f"{base_url}{url_params}"
            
            qr.add_data(qr_data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Sauvegarde de l'image
            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)
            
            # Encodage en base64 pour l'affichage direct
            img_str = base64.b64encode(buffer.getvalue()).decode('ascii')
            
            # Sauvegarde en DB
            media_path = f'qrcodes/mixx_{agent_number}.png'
            full_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes')
            os.makedirs(full_path, exist_ok=True)
            
            with open(os.path.join(settings.MEDIA_ROOT, media_path), 'wb') as f:
                f.write(buffer.getvalue())
            
            qr_code = QRCode.objects.create(
                operator='mixx',
                qr_image=media_path,
                data=data
            )
            
            return render(request, 'agent/qr_display.html', {
                'qr_code': qr_code,
                'img_data': img_str,
                'operator': 'MixxByYas'
            })
        
        return render(request, 'agent/mixx_form.html', {'form': form})

class MoovAgentFormView(View):
    def get(self, request):
        form = MoovAgentForm()
        return render(request, 'agent/moov_form.html', {'form': form})
    
    def post(self, request):
        form = MoovAgentForm(request.POST)
        if form.is_valid():
            client_number = form.cleaned_data['client_number']
            amount = form.cleaned_data['amount']
            agent_number = form.cleaned_data['agent_number']
            
            # Création des données à encoder dans le QR
            data = {
                'operator': 'moov',
                'client_number': client_number,
                'amount': str(amount),
                'agent_number': agent_number
            }
            
            # Création du QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            
            # Création d'une URL avec les paramètres
            base_url = request.build_absolute_uri(reverse('client:process_moov'))
            url_params = f"?client_number={client_number}&amount={amount}&agent_number={agent_number}"
            qr_data = f"{base_url}{url_params}"
            
            qr.add_data(qr_data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Sauvegarde de l'image
            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)
            
            # Encodage en base64 pour l'affichage direct
            img_str = base64.b64encode(buffer.getvalue()).decode('ascii')
            
            # Sauvegarde en DB
            media_path = f'qrcodes/moov_{client_number}_{amount}.png'
            full_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes')
            os.makedirs(full_path, exist_ok=True)
            
            with open(os.path.join(settings.MEDIA_ROOT, media_path), 'wb') as f:
                f.write(buffer.getvalue())
            
            qr_code = QRCode.objects.create(
                operator='moov',
                qr_image=media_path,
                data=data
            )
            
            return render(request, 'agent/qr_display.html', {
                'qr_code': qr_code,
                'img_data': img_str,
                'operator': 'Moov Money Flooz'
            })
        
        return render(request, 'agent/moov_form.html', {'form': form})