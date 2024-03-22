from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import  Product, KindProduct, Client #User,
from .forms import *

# Create your views here.
#from django.contrib.auth



def index(request):
    return render(request, 'base.html', {'data':'Hello'}) 


# def clients(request):

#     clients = Client.objects.all()
#     print(*clients)
#     for client in clients:
#         print(client.first_name)
#         print(client.last_name)
#         print(client.id)
#     return render(request, 'clients.html', {'clients': clients})

def clients(request, id):

    if id:
        client = Client.objects.get(id=id)
        print('Наш один клиент:',client)
        return render(request, 'client.html', {'client':client})
    
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

    products = Product.objects.all()
    print(*products)
    return render(request, 'products.html', {'products': products})

class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products' #или #object_list

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context['menu'] = ['menu1', 'menu2']
    #     return context
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     return Product.objects.filter(id=5)


class ClientAdd(CreateView):
    form_class = AddClientForm
    template_name = 'form_add_client.html'
    success_url = reverse_lazy('clients')



class Show_product(DetailView):
    model = Product
    template_name = 'product.htmpl'
    pk_url_kwarg = 'id'


def client_products(request):

    client = Client.objects.all()
    products = Product.objects.all()
    print(*client)
    print(*products)
    return render(request, 'client_products.html', {'products': products, 'client': client})


def product_add_view(request):
    if request.method == 'POST':
        form = AddProductForm2(request.POST)
        if form.is_valid():
            
            # если с моделью
            form.save()
            return redirect('products')
    
            #если без модели
            # print(form.cleaned_date)
            # try:
            #     Product.objects.create(**form.cleaned_data)
            #     return redirect('products')
            # except Exception as e:
            #     print('Ошибка', e)
            #     form.add_error(None, "Ошибка....")
    else:
        form = AddProductForm2()
    return render(request, 'form_add_product.html', {'form':form})        

def product_edit_view(request, id):
    product = get_object_or_404(Product, id=id)
    print(product)
    if request.method == 'GET':
        return render(
            request,
            'form_add_product.html',
            {'form':AddProductForm2(instance=product), 'id':id}
        )



# class RegisterClient(CreateView):
#     form_class = ClientCreationForm
#     template_name = 'client_reg.html'
#     #success_url = reverse_lazy('login')
    
#     def from_valid(self, form):
#         client = form.save()
#         login(self.request, client)
#         return redirect('index')
    
# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'form_login.html'

#     def get_succes_url(self):
#         return reverse_lazy('index')

# def logout_user(r):
#     logout(r)
#     return redirect('login')
