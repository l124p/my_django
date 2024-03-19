from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, KindProduct

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


def registration(request):
    if request.method == 'GET':
        return render(request, 'client_reg.html')
    if request.method == 'POST':
        last_name = request.POST.getlist('last_name')
        first_name = request.POST.getlist('first_name')
        age = request.POST.getlist('age')
        print('наш клиент',  last_name, first_name, age)
        return render(request, 'base.html')

def products(request):

    products = KindProduct.objects.all()
    print(*products)
    return render(request, 'products.html', {'products': products})


def client_products(request):

    client = Client.objects.all()
    products = KindProduct.objects.all()
    print(*client)
    print(*products)
    return render(request, 'client_products.html', {'products': products, 'client': client})
