from django.contrib import admin
from .models import Client, Product, KindProduct, ClientProduct
# Register your models here.

# @admin.register(User)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name')
#     search_fields = ('last_name__startwith', 'first_name__startwith')
#     list_filter = ['last_name']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ('last_name__startwith', 'first_name__startwith')
    list_filter = ['last_name']

    # def average_grade(self, obj):
    #     from django.db.models import Avg
    #     res = Grade.objects.filter(client=obj).aggregate(Avg('grade', default=0))
    #     return res['grade__avg']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(KindProduct)
class KindProductAdmin(admin.ModelAdmin):
    pass
    #list_display = ('name', 'course_num')
    #search_fields = ('name',)

@admin.register(ClientProduct)
class ClientProductAdmin(admin.ModelAdmin):
    pass