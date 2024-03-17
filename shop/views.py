from django.shortcuts import render
from django.http import HttpResponse
from .models import Client

# Create your views here.


def index(request):
    return render(request, 'base.html', {'data':'Hello'}) 


def clients(request):

    clients = Client.objects.all()
    print(*clients)
    for client in clients:
        print(client.first_name)
        print(client.last_name)
        print(client.id)
    return render(request, 'clients.html', {'clients': clients})
