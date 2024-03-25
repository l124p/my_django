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

from django.http import HttpResponse, HttpResponseRedirect

from .models import  Product, KindProduct
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


class ShowProduct(DetailView):
    model = Product
    template_name = 'product.html'
    pk_url_kwarg = 'id'


class ProductAdd(LoginRequiredMixin, CreateView):
    form_class = AddProductForm2
    template_name = 'form_add_product.html'
    success_url = reverse_lazy('products')
    login_url = '/login/'


@login_required(login_url='/login/')
def client_products(request):
    if request.method == 'POST':
        form = AddProductClient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
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
    template_name = 'form_reg_user.html'
    # success_url = reverse_lazy('index')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  
        return HttpResponseRedirect(reverse_lazy('index'))
        # return redirect('index')
        #return HttpResponse('Form not valid')


class LoginUser(LoginView):
    print("Перенаправляем на loginview")
    form_class = AuthenticationForm
    template_name = 'form_login.html'
    def get_succes_url(self):
        return reverse_lazy('index')

    

def logout_user(r):
    logout(r)
    return redirect('login')


