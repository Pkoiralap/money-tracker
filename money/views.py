from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaction


def home_page(request):
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


def show(request):
    return HttpResponse('<h1> Show Page </h1>')