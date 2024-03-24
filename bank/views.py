from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.exceptions import ValidationError


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView 
from django.contrib.auth import login, logout

from django.http import HttpResponse

from .models import  Product, KindProduct, Client #User,
from .forms import *

# Create your views here.


def index(request):
    return render(request, 'base.html', {'data':'Hello'}) 


class Clients(ListView):
    model = Client
    template_name = 'clients.html'
    context_object_name = 'clients' #или #object_list


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ShowClient(DetailView):
    model = Client
    template_name = 'client.html'
    pk_url_kwarg = 'id'
    id_client=0
    def get_object(self, queryset=None):
        # Access the captured 'pk' parameter from the URL using 'self.kwargs'
        id_client = self.kwargs.get(self.pk_url_kwarg)
        return Client.objects.get(pk=id_client)
        
    print('наш клиент id', id_client)   
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        
        print('наш контекст 1',context)
        print('наш клиент id', id_client) 
        products = ClientProduct.objects.filter(client_id=id)
        print(products)
        print('наш контекст 2',context)
        return context

def clients(request, id):

    if id:
        client = Client.objects.get(id=id)
        products = ClientProduct.objects.filter(client_id=id)
        return render(request, 'client.html', {'client':client, 'products': products})
    
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


class ClientAdd(LoginRequiredMixin, CreateView):
    form_class = AddClientForm
    template_name = 'form_add_client.html'
    success_url = reverse_lazy('clients')
    login_url = '/login/'


class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products' #или #object_list


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context['menu'] = ['menu1', 'menu2']
    #     return context
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     return Product.objects.filter(id=5)


class ShowProduct(DetailView):
    model = Product
    template_name = 'product.html'
    pk_url_kwarg = 'id'

class ProductAdd(LoginRequiredMixin, CreateView):
    form_class = AddProductForm2
    template_name = 'form_add_product.html'
    success_url = reverse_lazy('products')
    login_url = '/login/'


# @login_required(login_url='/login/')
# def client_products(request, id):
#     request.user.username
#     client = get_object_or_404(Client, id=id)
#     print(client)
#     #client = Client.objects.all()
#     products = Product.objects.all()
#     print(*client)
#     print(*products)
#     return render(request, 'client_products.html', {'products': products, 'client': client})

@login_required(login_url='/login/')
def client_products(request):
    selected_client = None
    print(request.method)
    if request.method == 'GET':
        clients = Client.objects.all()
        return render(request, 'client_products.html', {'clients': clients})
    if request.method == 'POST':
        if not request.POST.get("product"):
            selected_client = request.POST.get("client")
            print('Выбранный клиент',selected_client)
            client = Client.objects.filter(id=selected_client)
            print('Select клиент',client)
            #products_client = products.filter(client=selected_client)
            products = Product.objects.all()
            kind_products = KindProduct.objects.all()
            print(kind_products)
            print(*products)
            print(type(selected_client))
            context = {
                'products': products,
                'selected_client': selected_client,
                'kind_products': kind_products
                }
            return render(request, 'client_products.html',context )
        id = request.POST.get("client_id")
        print('Клиент:', id)
        print('Продукт:',request.POST.get("product"))

        form = AddProductClient(request.POST)
        print(form)
        if form.is_valid():
            
            # если с моделью
            form.save()
            return redirect('products')
                    #если без модели
        # form = AddProductClient(request.POST)
        # if form.is_valid():
        #     print(form.cleaned_date)
        #     try:
        #         ClientProduct.objects.create(**form.cleaned_data)
        #         return redirect('client_products.html')
        #     except Exception as e:
        #         print('Ошибка', e)
        #         form.add_error(None, "Ошибка....")
        # else:
        #     print('Ошибка:',form.cleaned_date)
        #     form = AddProductClient()    
        #     return render(request, 'client_products.html', {'form':form})    
        return redirect('index')



def client_products_1(request):
    if request.method == 'POST':
        form = AddProductClient(request.POST)
        if form.is_valid():
            
            # если с моделью
            form.save()
            return redirect('products')
    
            # #если без модели
            # print(form.cleaned_date)
            # try:
            #     Product.objects.create(**form.cleaned_data)
            #     return redirect('products')
            # except Exception as e:
            #     print('Ошибка', e)
            #     form.add_error(None, "Ошибка....")

    else:
        form = AddProductClient()
    return render(request, 'form_add_clientproduct.html', {'form':form})   



@login_required(login_url='/login/')
def product_edit_view(request, id):
    request.user.username
    product = get_object_or_404(Product, id=id)
    print(product)
    if request.method == 'GET':
        return render(
            request,
            'form_add_product.html',
            {'form':AddProductForm2(instance=product), 'id':id}
        )


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'form_reg_client.html'

    def from_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')



class LoginUser(LoginView):
    print("Перенаправляем на loginview")
    form_class = AuthenticationForm
    template_name = 'form_login.html'
    print("Перенаправляем на 1")
    def get_succes_url(self):
        print("Перенаправляем на index")
        return reverse_lazy('index')
    print("Перенаправляем на 2")
    

def logout_user(r):
    logout(r)
    return redirect('login')


