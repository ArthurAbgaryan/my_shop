from django.urls import path
from .views import coupon
app_name = 'coupon'

urlpatterns = [
    path('coupon/',coupon, name = 'coupon_apply'),

]