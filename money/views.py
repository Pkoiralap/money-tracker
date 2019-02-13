from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from .models import Transaction

class TransactionForm(forms.Form):
    type = forms.ChoiceField(
        choices=(('income', 'Income'), ('expenditure', 'Expenditure')),
        widget=forms.Select
    )
    giving = forms.CharField(label='Giving', max_length="100", min_length="5")
    receiving = forms.CharField(label='Receiving', max_length="100", min_length="5")
    date = forms.DateTimeField(label='Date')
    money = forms.FloatField(label='Money')



def index(request):
    context = {
        'allPeople': [
            {
                'name': 'Nished',
                'occupation': 'Engineer'
            },
            {
                'name': 'Suyog',
                'occupation': 'Doctor'
            },
            {
                'name': 'Kedar',
                'occupation': 'Physicist'
            }
        ],
        'allFacilitators': [
            {
                'name': 'Adarsh',
                'occupation': 'Engineer'
            },
            {
                'name': 'Prasanna',
                'occupation': 'Engineer'
            }
        ],
        'transactions': Transaction.objects.all()
    }
    return render(request, 'index.html', context)


def view_transactions(request):
    return render(request, 'view_transactions.html', {'transactions': Transaction.objects.all()})

def add_transaction(request):
    context = {
        'form': TransactionForm()
    }
    if request.method == 'POST':
        new_trans = Transaction()
        new_trans.type = request.POST.get('type')
        new_trans.giving_party = request.POST.get('giving')
        new_trans.receiving_party = request.POST.get('receiving')
        new_trans.date = request.POST.get('date')
        new_trans.money = request.POST.get('money')
        new_trans.save()

    return render(request, 'add_transaction.html', context)

def remove_transaction(request):
    if request.method == 'POST':
        key = request.POST.get('primary_key')
        trans_obj = Transaction.objects.filter(pk=key)
        trans_obj.delete()
    context = {
        'transactions': Transaction.objects.all()
    }

    return render(request, 'view_transactions.html', context)

def home_page(request):
    return render(request, 'base.html', {})