
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('payment.urls', namespace='payment')),
    path('',include('shop.urls',namespace = 'shop')),
    path('cart/',include('cart.urls', namespace='cart')),
    path('order/', include('orders.urls', namespace='order')),
    path('coupon/',include('coupon.urls',namespace='coupon')),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
