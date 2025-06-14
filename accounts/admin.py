from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import BankAccount, Transaction

admin.site.register(BankAccount)
admin.site.register(Transaction)