from django.urls import path
from .views import payment_done,payment_canceled,payment_process
app_name = 'payment'

urlpatterns = [
    path('paument_done/', payment_done,name = 'done' ),
    path('canceled/', payment_canceled, name = 'canceled'),
    path('process/', payment_process, name = 'process'),
]