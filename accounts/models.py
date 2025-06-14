from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank_accounts')
    iban = models.CharField(max_length=34, unique=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.iban}"

class Transaction(models.Model):
    TRANSFER_OUT = 'TRANSFER_OUT'
    TRANSFER_IN = 'TRANSFER_IN'

    TRANSACTION_TYPES = [
        (TRANSFER_OUT, 'Transfer Out'),
        (TRANSFER_IN, 'Transfer In'),
    ]

    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    transaction_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.account.iban}"