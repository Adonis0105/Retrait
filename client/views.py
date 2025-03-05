# client/views.py
from django.shortcuts import render, redirect
from django.views import View
from .forms import MixxClientForm, MoovClientForm
from django.http import HttpResponseRedirect

class ScanQRView(View):
    def get(self, request):
        return render(request, 'client/scan_qr.html')

class ProcessMixxQRView(View):

    def get(self, request):
        agent_number = request.GET.get('agent_number', '')
        if not agent_number:
            return redirect('client:scan')

        form = MixxClientForm()
        return render(request, 'client/mixx_form.html', {
            'form': form,
            'agent_number': agent_number,
            'transaction_code': None  # On initialise sans code
        })

    def post(self, request):
        agent_number = request.GET.get('agent_number', '')
        form = MixxClientForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['amount']
            personal_code = form.cleaned_data['personal_code']

            # Génération du code USSD
            transaction_code = f"*145*2*{amount}*{agent_number}*{personal_code}#"

            # On renvoie directement le code pour qu'il s'affiche sur la page
            return render(request, 'client/mixx_form.html', {
                'form': form,
                'agent_number': agent_number,
                'transaction_code': transaction_code  # On passe le code à la page
            })

        return render(request, 'client/mixx_form.html', {
            'form': form,
            'agent_number': agent_number,
            'transaction_code': None
        })
    
class ProcessMoovQRView(View):
    def get(self, request):
        agent_number = request.GET.get('agent_number', '')
        
        if not agent_number:
            return redirect('client:scan')
            
        form = MoovClientForm()
        return render(request, 'client/moov_form.html', {
            'form': form,
            'agent_number': agent_number,
            'transaction_code': None  # On initialise sans code
        })
    
    def post(self, request):
        agent_number = request.GET.get('agent_number', '')
        form = MoovClientForm(request.POST)
        
        if form.is_valid():
            secret_code = form.cleaned_data['secret_code']
            
            # Construction du code de transaction
            transaction_code = f"*155*5*1*{secret_code}#"
            
            # On renvoie directement le code pour qu'il s'affiche sur la page
            return render(request, 'client/moov_form.html', {
                'form': form,
                'agent_number': agent_number,
                'transaction_code': transaction_code  # On passe le code à la page
            })
        
        return render(request, 'client/moov_form.html', {
            'form': form,
            'agent_number': agent_number,
            'transaction_code': None
        })