from django.shortcuts import render
from .forms import CartAddProductForm
from django.shortcuts import get_object_or_404,redirect
from .cart import Cart
from shop.models import Product
from django.views.decorators.http import require_POST

'''Добавление товара '''
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
        return redirect ('cart:cart_detail')

'''Удаление товара'''
def cart_remove(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart:cart_detail')


'''Отображение всех товаров карзины на основе данных сохраненных в request.session
Так же создана форма для управления кол-во товара в корзине
'''
def cart_detail(request):
    cart = Cart(request)
    for i in cart:
        i['qunty_form'] = CartAddProductForm(initial={'quantity': i['quantity'], 'update':True})
    return render(request, 'cart/detail.html', {'cart_cart':cart})
# Create your views here.
