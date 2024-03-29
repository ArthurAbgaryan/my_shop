import requests
from django.conf import settings
from shop.models import Product
from decimal import Decimal
from coupon.models import Coupon

class Cart(object):

    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')

    def add(self, product,quantity = 1, update_quantity = False):
        """Добавление товара в корзину или обновление"""
        product_id = str(product.id) #получаем строковое id для json ключа, т.к. у json ключи в строковом форм.
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' :0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        '''Помечаем сессию как измененной'''
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):
        '''Проходим по товарам корзины и получаем соответсвующие обьекты Product'''
        product_ids = self.cart.keys()
        '''Получаем обьекты модели Product и передаем их в корзину'''
        products = Product.objects.filter(id__in = product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        if cart:
            for item in cart.values():
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * item['quantity']
                yield item

    def __len__(self):
        '''Возвращаем общее кол-во товаров в корзине'''
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

    def clear(self):
        '''Очистка корзины'''
        del self.session[settings.CART_SESSION_ID]
        self.save()
    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id = self.coupon_id)
        return None

    def coupon_discounter(self):
        if self.coupon_id:
            return (self.coupon.discount/Decimal('100'))*self.get_total_price()
        return Decimal('0')

    def total_price_with_discounter(self):
        return (self.get_total_price()-self.coupon_discounter())


