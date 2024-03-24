from django.db import models

from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator, \
                                   validate_email, validate_slug

from django.contrib.auth.models import AbstractUser
# Create your models here.
class Person(models.Model):
    last_name = models.CharField(max_length=30,
                                 #null=False,
                                 # blank=False 
                                 verbose_name = 'Имя'
                                  )
    first_name = models.CharField(max_length=30,
                                 # null=False,
                                  #blank=False
                                  verbose_name = 'Фамилия'
                                  )
    age = models.PositiveSmallIntegerField(
        default=None,
        verbose_name = 'Возраст',
        validators=[MinValueValidator(18), MaxValueValidator(120)]
    )
    
    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.age}'
    

    class Meta:
        indexes = [models.Index(fields=['first_name']) ]
        #ordering = [models.OrderBy(fields=['first_name'])]
        ordering = ['first_name']
        abstract = True

class Client(Person):
#class Client(AbstractUser):

    address = models.CharField(max_length=255,blank=True)
    phone  = models.CharField(max_length=15,blank=True)

    def get_absolute_url(self):
        return reverse('client', kwargs={'id': self.pk})
    
    class Meta:
        #ordering = [models.OrderBy(fields=['first_name'])]
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        db_table = 'clients'


# class Employer(AbstractUser):
#     department = models.CharField(max_length=255)
#     phone  = models.CharField(max_length=15)



class KindProduct(models.Model):

    name = models.CharField(max_length=25, blank=True, default=None, verbose_name = 'Название вида продукта' )
    def __str__(self) -> str:
        return f'{self.name}'  
    class Meta:
        unique_together= ('name',)
        ordering = ['name']
        verbose_name = "Вид продукта"
        verbose_name_plural = "Виды продуктов"
        db_table = 'kind_products'


class Product(models.Model):
    name = models.CharField(max_length=30,
                                 #null=False,
                                 blank=True,
                                verbose_name = 'Название продукта' 
                                  )
    kind_product = models.ForeignKey(KindProduct, on_delete=models.CASCADE, verbose_name = 'Вид продукта', blank=True, default=None)
    #start_date = models.DateField(null=True,blank=True)
    #end_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(verbose_name = 'Срок действия', default='2099-12-31')
    description = models.TextField(blank=True, verbose_name = 'Описание продукта')
    class Meta:
        unique_together = ('name', 'kind_product')
        ordering = ['kind_product', 'name']
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        db_table = 'product'

    def __str__(self) -> str:
        return f'{self.kind_product} {self.name}'
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'id': self.pk})


class ClientProduct(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)   # дата открытия

    def __str__(self) -> str:
        return f'У {self.client.first_name} {self.client.last_name} открыт {self.product} - {self.date}'
    class Meta:
        verbose_name = "Продукт клиента"
        verbose_name_plural = "Продукты клиентов"