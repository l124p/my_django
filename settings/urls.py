"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from bank import views
from bank.views import *
#from bank.forms import RegistrClientForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    #path('reg/', RegistrClient.as_view, name='registration'),
    #path('login/', LoginClient.as_view, name='login'),
    #path('logout/', logout_user, name='logout'),
    path('clients/', views.clients, name='clients', kwargs={'id':0}),
    path('client/<int:id>', views.clients, name='client'),
    # path('client/add', views.clients, name='addclient'),
    path('client/add', ClientAdd.as_view(), name='addclient'),
    path('client/edit/<int:id>', views.clients, name='editclient'),

    #path('users/', views.users, name='users'),

    #path('products/', views.products, name='products'),
    #path('product/<int:id>', views.clients, name='product'),
    path('product/add', product_add_view, name='addproduct'),
    # path('product/edit/<int:id>', views.clients, name ='editproduct'),
    path('product/edit/<int:id>', product_edit_view, name ='editproduct'),

    path('products/', Products.as_view(), name='products'),
    path('product/<int:id>', Show_product.as_view(), name='product'),
  
    path('client_products/', views.client_products, name='client_products'),
]

if settings.DEBUG:
#    urlpatterns = [path("__debug__/", include("debug_toolbar.urls")),] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns = [path("__debug__/", include("debug_toolbar.urls")),] + urlpatterns