from django.shortcuts import render
from .models import OrderItem
from .forms import OrderItemForm
from cart.cart import Cart
from .tasks import order_created

def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order = order,
                                        product = item['product'],
                                        price = item['price'],
                                        quantity = item['quantity'])
            cart.clear()
            order_created.delay(order.id) #delay метод для запуска ассинхронной задачи
            return render(request, 'orders/created.html',{'order':order})
    else:
        form = OrderItemForm()
    return render(request,'orders/create.html', {'cart':cart, 'form':form} )

# Create your views here.
