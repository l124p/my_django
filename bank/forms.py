from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.contrib.auth.models import Client

from .models import *

class AddProductForm(forms.Form):
    name = forms.CharField(label="Название продукта")
    kind_product = forms.ModelChoiceField(
        queryset=KindProduct.objects.all(),
        label="Вид продукта",
        empty_label='Вид продукта не выбран'
    )
    # start_date = forms.DateField(widget=forms.DateInput(
    #                                attrs={'type':'date',
    #                                      'placeholder':'01.01.2023'}
    #                                     )
    #                             )
    end_date = forms.DateField(widget=forms.SelectDateWidget,label="Срок действия")
    descripton = forms.CharField(
        widget=forms.Textarea(attrs={'cools':30,'rows':5}),
        label="Описание продукта",
        required=False
        )
    # user = forms.ModelChoiceField(
    #     queryset=Client.objects.all(),
    #     empty_label='Клиент не выбран'
    # )

class AddProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ['name', 'kind_product']



class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        #fields = ['name', 'course_num']
    # def clean_age(self):
    #     age = self.cleaned_data['age']
    #     if age == 22 or age == 33:
    #         raise ValidationError('Возраст не подходит')
    #     widgets = {
    #         'age':forms.DateInput{
    #             attrs={'type':'date', 'class':'date_label'}
    #         }
    #     }

class RegistrClientForm(UserCreationForm):
    model = Client
    fields = '__all__'
