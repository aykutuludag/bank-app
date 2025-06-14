from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import BankAccount

def bank_accounts_list(request):
    accounts = BankAccount.objects.all()
    data = []
    for acc in accounts:
        data.append({
            'user': acc.user.username,
            'iban': acc.iban,
            'balance': float(acc.balance),
        })
    return JsonResponse(data, safe=False)