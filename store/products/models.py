from django.db import models
from users.models import User

# Create your models here.
# модели = таблицы

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)  # =пустой те можно поле оставить пустым или добавить описание

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)   # значения до и после запятой
    quantity = models.PositiveIntegerField(default=0)    # positive количество товаров не может быть отриц
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)    # протект - товары останутся при удалении категории

    def __str__(self):
        return f'{self.name} | {self.category.name}'

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Basket for {self.user.username} | Product {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price