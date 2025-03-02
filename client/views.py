# client/views.py
from django.shortcuts import render, redirect
from django.views import View
from .forms import MixxClientForm, MoovClientForm

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
            'agent_number': agent_number
        })
    
    def post(self, request):
        agent_number = request.GET.get('agent_number', '')
        form = MixxClientForm(request.POST)
        
        if form.is_valid():
            amount = form.cleaned_data['amount']
            personal_code = form.cleaned_data['personal_code']
            
            # Construction du code de transaction
            transaction_code = f"*145*2*{amount}*{agent_number}*{personal_code}#"
            
            return render(request, 'client/transaction_code.html', {
                'transaction_code': transaction_code,
                'operator': 'MixxByYas'
            })
        
        return render(request, 'client/mixx_form.html', {
            'form': form,
            'agent_number': agent_number
        })

class ProcessMoovQRView(View):
    def get(self, request):
        client_number = request.GET.get('client_number', '')
        amount = request.GET.get('amount', '')
        agent_number = request.GET.get('agent_number', '')
        
        if not all([client_number, amount, agent_number]):
            return redirect('client:scan')
            
        form = MoovClientForm()
        return render(request, 'client/moov_form.html', {
            'form': form,
            'client_number': client_number,
            'amount': amount,
            'agent_number': agent_number
        })
    
    def post(self, request):
        client_number = request.GET.get('client_number', '')
        amount = request.GET.get('amount', '')
        agent_number = request.GET.get('agent_number', '')
        
        form = MoovClientForm(request.POST)
        
        if form.is_valid():
            secret_code = form.cleaned_data['secret_code']
            
            # Construction du code de transaction
            transaction_code = f"*155*5*1*{secret_code}#"
            
            return render(request, 'client/transaction_code.html', {
                'transaction_code': transaction_code,
                'operator': 'Moov Money Flooz'
            })
        
        return render(request, 'client/moov_form.html', {
            'form': form,
            'client_number': client_number,
            'amount': amount,
            'agent_number': agent_number
        })