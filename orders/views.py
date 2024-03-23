from django.shortcuts import render,redirect
from .models import OrderItem
from .forms import OrderItemForm
from cart.cart import Cart
from django.urls import reverse
# from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from orders.models import Order

@staff_member_required
def admin_ite(request,order_id):
    order = get_object_or_404(Order, id = order_id)
    return render(request, 'admin/order_detail.html', {'order':order})

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
            request.session['order_id'] = order.id #сохранение заказа в сессии
            return redirect(reverse('payment:process'))

            # return render(request, 'orders/created.html',{'order':order})
    else:
        form = OrderItemForm()
    return render(request,'orders/create.html', {'cart':cart, 'form':form} )

# Create your views here.
