"""
URL configuration for bank_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    bank_accounts_list,
    account_list_page,
    transaction_list_page,
    group_list_page,
    user_list_page
)

urlpatterns = [
    path('accounts/', bank_accounts_list, name='bank_accounts_list'),
    path('accounts/ui/', account_list_page, name='account_list_page'),
    path('transactions/ui/', transaction_list_page, name='transaction_list_page'),
    path('groups/ui/', group_list_page, name='group_list_page'),       # <--- Burada
    path('users/ui/', user_list_page, name='user_list_page'),          # <--- Burada
]
