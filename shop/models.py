from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, \
                                   validate_email, validate_slug

# Create your models here.

class Person(models.Model):
    last_name = models.CharField(max_length=30,
                                 #null=False,
                                 # blank=False 
                                  )
    first_name = models.CharField(max_length=30,
                                 # null=False,
                                  #blank=False
                                  )
    age = models.PositiveSmallIntegerField(
        default=None,
        validators=[MinValueValidator(18), MaxValueValidator(120)]
    )
    
    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.age}'

    class Meta:
        indexes = [models.Index(fields=['first_name']) ]
        #ordering = [models.OrderBy(fields=['first_name'])]
        abstract = True

class Client(Person):
    #kind_product = models.ManyToManyField('KindProduct', default=None)
    products = models.ManyToManyField('KindProduct', through="ClientProduct")
    class Meta:
        #ordering = [models.OrderBy(fields=['first_name'])]
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        db_table = 'clients'



class ClientProduct(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey('KindProduct', on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)   # дата открытия

    def __str__(self) -> str:
        return f'У {self.client.first_name} {self.client.last_name} открыт {self.product} - {self.date}'
    
    class Meta:
        verbose_name = "Продукт клиента"
        verbose_name_plural = "Продукты клиентов"


    
class Product(models.Model):

    name = models.CharField(max_length=25, blank=True, default=None)
    #course_num = models.SmallIntegerField(default=None)

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        unique_together= ('name',)
        ordering = ['name']
        verbose_name = "Вид продукта"
        verbose_name_plural = "Виды продуктов"
        #db_table = 'products'



class KindProduct(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    kind = models.CharField(max_length=30,
                                 #null=False,
                                 # blank=False 
                                  )
    class Meta:
        unique_together = ('product', 'kind')
        #ordering = [models.OrderBy(fields=['first_name'])]
        ordering = ['product', 'kind']
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        #db_table = 'KindProduct'

    def __str__(self) -> str:
        return f'{self.product} {self.kind}'


class ModelsCategory(models.Model):
    pass