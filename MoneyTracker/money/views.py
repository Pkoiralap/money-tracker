from django.shortcuts import render
from os import path

# Create your views here.
base_address = path.dirname(__file__) + '/templates/'

def index(request):
    return render(request, 'money/index.html', {})


def past_transactions(request):
    context = {}
    return render(request, 'money/index.html', context)


def add_transactions(request):
    context = {}
    return render(request, 'money/index.html', context)
