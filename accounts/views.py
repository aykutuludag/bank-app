from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import BankAccount, Transaction
from django.contrib.auth.models import User, Group

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


def account_list_page(request):
    accounts = BankAccount.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})


def transaction_list_page(request):
    transactions = Transaction.objects.select_related('account__user').all()
    return render(request, 'accounts/transaction_list.html', {'transactions': transactions})

def group_list_page(request):
    groups = Group.objects.prefetch_related('members').all()
    return render(request, 'accounts/group_list.html', {'groups': groups})


def user_list_page(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})