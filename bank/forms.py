from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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


#class RegisterUserForm(UserCreationForm):
#    model = User
#    fiels = '__all__'

#class UserRegisetrForm(UserCreationForm):
class RegisterUserForm(UserCreationForm):
    #confirm_password = forms.CharField(widget=forms.PasswordInput)    
    #password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    email = forms.CharField(required=True)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        #self.fields['password'].label = 'Пароль'
        #self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['first_name'].label = 'Ваше имя'
        self.fields['last_name'].label = 'Ваша фамилия'
        self.fields['address'].label = 'Адрес'
        self.fields['email'].labem = '"Электронная почта'

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if User.objects.filter(email=email).exist():
    #         raise forms.ValidationError(f'Почтовый адрес уже зарегистрирован')    
    #     return email
                
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if User.objects.filter(username=username).exist():
    #         raise forms.ValidationError(f'Имя {username} уже зарегистрирован')    
    #     return username
    # def clean(self):
    #     password = self.cleaned_data['password']
    #     confirm_password = self.cleaned_data['confirm_password']
    #     if password != confirm_password:
    #         raise forms.ValidationError(f'пароли не совпадают')    
    #     return self.cleaned_data
    
    class Meta:
        model = User
        fields = ['username','phone','first_name',
                  'last_name','address','email']