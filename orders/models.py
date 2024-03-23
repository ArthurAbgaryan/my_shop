from django.db import models
from shop.models import Product
'''Модель сщхраняет данные о покупателе'''
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False) #этом  поле в дальнейш. будем исп-ть как "оплачено/неоплачено"
    braintree_id = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return 'Order {}'.format(self.id)


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


'''Модель для сохранения данных каждого элемента корзины'''
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
# Create your models here.
