import braintree
from django.shortcuts import get_object_or_404,render,redirect
from orders.models import Order

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id = order_id)
    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None)#получение токена для создания транзакции
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce':nonce,
            'options':{
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            order.paid = True #отметка заказа как оплаченного в поле модели order
            order.braintree_id = result.transaction.id #сохранение ID транзакции в поле модели order
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        client_token = braintree.ClientToken.generate()
        return render(request, 'payment/process.html',{'order':order,'client_token':client_token})

def payment_done(request):
    return render(request,'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')

