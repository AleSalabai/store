from django.contrib import admin
from .models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)
# admin.site.register(Product)
admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    readonly_fields = ('short_description',)
    ordering = ('-name',)    # сортировка
    search_fields = ('name',)    # поле, по ктрм будем искать объект среди всех товаров


